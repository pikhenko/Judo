from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .models import Posts, Photo

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Посты", 'url_name': 'add_page'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Расписание", 'url_name': 'shedule'},
        {'title': "Наша команда", 'url_name': 'team'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'backend/index.html', context=context)


def add_page(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Посты'
    }
    return render(request, 'backend/posts.html', context=context)


def photo(request):
    photo = Photo.objects.all()
    
    return render(request, 'backend/photo.html', {'menu': menu, 'title': 'Фотогалерея', 'photo': photo})


def team(request):
    return render(request, 'backend/team.html', {'menu': menu, 'title': 'Наша команда'})


def shedule(request):
    return render(request, 'backend/shedule.html', {'menu': menu, 'title': 'Расписание'})


def about(request):
    return render(request, 'backend/about.html', {'menu': menu, 'title': 'О Нас'})


def read_post(request, post_id):
    posts = get_object_or_404(Posts, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
    }

    return render(request, 'backend/detail_post.html', context=context)

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    else:
        form = AddPostForm()
    return render(request, 'backend/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def login(request):
    return HttpResponse("Авторизация")
