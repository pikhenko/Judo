from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

<<<<<<< HEAD
from .models import *
from .forms import *

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Посты", 'url_name': 'post_list'}, 
        {'title': "Фотогалерея", 'url_name': 'photo'}, 
        {'title': "Расписание", 'url_name': 'shedule'}, 
=======
from .models import Posts, Photo

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "Посты", 'url_name': 'add_page'},
        {'title': "Фотогалерея", 'url_name': 'photo'},
        {'title': "Расписание", 'url_name': 'shedule'},
>>>>>>> 80b08dbb6b766f69fd5783439bdc45c52f8b35fe
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

<<<<<<< HEAD
def post_list(request):
=======

def add_page(request):
>>>>>>> 80b08dbb6b766f69fd5783439bdc45c52f8b35fe
    posts = Posts.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'menu': menu,
        'title': 'Посты'
    }
    return render(request, 'backend/posts.html', context=context)


def photo(request):
    photo = Photo.objects.all()
    paginator = Paginator(photo, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'backend/photo.html', {'menu': menu, 'title': 'Фотогалерея', 'page_obj': page_obj})


def team(request):
    return render(request, 'backend/team.html', {'menu': menu, 'title': 'Наша команда'})


def shedule(request):
    return render(request, 'backend/shedule.html', {'menu': menu, 'title': 'Расписание'})


def about(request):
    return render(request, 'backend/about.html', {'menu': menu, 'title': 'О Нас'})

<<<<<<< HEAD
def read_post(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
=======

def read_post(request, post_id):
    posts = get_object_or_404(Posts, pk=post_id)
>>>>>>> 80b08dbb6b766f69fd5783439bdc45c52f8b35fe

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
