from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required   
from .models import *
from .forms import AddPostForm, CommentForm

menu = [{'title': "Главная", 'url_name': 'backend:home'},
        {'title': "Посты", 'url_name': 'backend:post_list'},
        {'title': "Фотогалерея", 'url_name': 'backend:photo'},
        {'title': "Расписание", 'url_name': 'backend:shedule'},
        {'title': "Наша команда", 'url_name': 'backend:team'},
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
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
    photo = Photo.objects.all()
    paginator = Paginator(photo, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'backend/photo.html', {'menu': menu, 'title': 'Фотогалерея', 'page_obj': page_obj})

def team(request):
    return render(request, 'backend/team.html', {'menu': menu, 'title': 'Наша команда'})


def shedule(request):
    return render(request, 'backend/shedule.html', {'menu': menu, 'title': 'Расписание'})


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
        comment.post = post
        comment.save()
    return render(request, 'backend/comment.html',
                            {'post': post,
                             'form': form,
                             'comment': comment})


def signup(request):
    return render(request, 'users/signup.html')
