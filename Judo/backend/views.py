from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *
from .models import Category, PhotoGallery, News
from users.models import Profile
from .forms import AddPostForm, CommentForm, PhotoForm, ContactForm


menu = [{'title': "Главная", 'url_name': 'backend:home'},
        # {'title': "Посты", 'url_name': 'backend:post_list'},
        {'title': "Фотогалерея", 'url_name': 'backend:gallery'},
        {'title': "Расписание", 'url_name': 'backend:shedule'},
        {'title': "О тренере", 'url_name': 'backend:team'},
        ]


def index(request):
    posts = Posts.objects.order_by('time_create')[:2]
    news_list = News.objects.all()
    day_of_week = datetime.today().weekday()
    days = days = ['Понедельник', 'Вторник', 'Среда',
                   'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    try:
        schedule = Schedule.objects.get(day=days[day_of_week])
        context = {
            'menu': menu,
            'title': 'Главная страница',
            'message': 'сегодня тренировка',
            'address': schedule.address,
            'time': schedule.time,
            'posts': posts,
            'news_list' : news_list,
        }
    except Schedule.DoesNotExist:
        context = {
            'menu': menu,
            'title': 'Главная страница',
            'message': 'сегодня нет тренировок',
            'posts': posts,
            'news_list' : news_list,
        }
    return render(request, 'backend/index.html', context=context)


def post_list(request):
    posts = Posts.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'menu': menu,
        'title': 'Посты',
    }
    return render(request, 'backend/posts.html', context=context)


def photo(request):
    form = PhotoForm(
            request.POST,
            files=request.FILES or None
        )
    photo = PostsPhoto.objects.all()
    paginator = Paginator(photo, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'backend/photo.html', {'menu': menu, 'title': 'Фотогалерея', 'page_obj': page_obj, 'form': form})


def team(request):
    return render(request, 'backend/team.html', {'menu': menu, 'title': 'О тренере'})


def shedule(request):
    profile = Profile.objects.get(user=request.user)
    schedules = Schedule.objects.filter(age_group=profile.age_group)
    return render(request, 'backend/shedule.html', {'menu': menu,
                                                    'title': 'Расписание',
                                                    'schedules': schedules})


def read_post(request, post_slug):
    post = get_object_or_404(Posts,
                             slug=post_slug)

    comments = post.comments.all()
    form = CommentForm()

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'comments': comments,
        'form': form,
    }

    return render(request, 'backend/detail_post.html', context)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backend:home')

    else:
        form = AddPostForm()
    return render(request, 'backend/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def login(request):
    return render(request, 'users/login.html')


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Posts,
                             id=post_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return render(request, 'backend/comment.html',
                            {'post': post,
                             'form': form,
                             'comment': comment})


def signup(request):
    return render(request, 'users/signup.html')


# @login_required(login_url='login')


def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        # photos = PhotoGallery.objects.filter(category__user=user)
        photos = PhotoGallery.objects.all()
    else:
        photos = PhotoGallery.objects.filter(
            category__name=category)

    # пагинатор
    paginator = Paginator(photos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # categories = Category.objects.filter(user=user)
    categories = Category.objects.all()

    # photo_pk = PhotoGallery.objects.get()
    # del_photo = photo_pk.delete()


    context = {'categories': categories, 'photos': photos, 'menu': menu, 'title': 'Фотоальбом', 'page_obj': page_obj}
    return render(request, 'backend/gallery.html', context)


@login_required(login_url='backend:login')
def view_photo(request, pk):
    photo = PhotoGallery.objects.get(id=pk)
    return render(request, 'backend/view_photo.html', {'menu': menu, 'photo': photo})


def delete_photo(request, pk):
    photo_pk = PhotoGallery.objects.get(id=pk)
    photo_pk.delete()
    return redirect('backend:gallery')


@login_required(login_url='login')
def add_photo(request):
    user = request.user
    categories = user.category_set.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = PhotoGallery.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )
        return redirect('backend:gallery')
    context = {'categories': categories}
    return render(request, 'backend/add.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Заказ звонка от {}'.format(name),
                'Номер телефона: {}'.format(phone),
                'Email: {}'.format(email),
                'Сообщение от {}'.format(message),
                'your-email@example.com',  # Адрес отправителя
                ['admin@example.com'],  # Адрес получателя
            )
    else:
        form = ContactForm()

    return render(request, 'backend/contact.html', {'form': form,
                                                    'title': 'Обратная связь',
                                                    'menu': menu})

def news(request):
    news_list = News.objects.all()
    context = {'news_list': news_list}
    return render(request, 'backend/news.html', context)