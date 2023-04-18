from django.http import HttpResponse
from django.shortcuts import render

menu = ["Главная страница", "Фотогалерея", "Расписание", "Наша команда", "Войти"]


def index(request):
    return render(request, 'backend/index.html', {'menu': menu, 'title': 'Главная страница'})


def photo(request):
    return render(request, 'backend/photo.html', {'menu': menu, 'title': 'Фотогалерея'})


def team(request):
    return render(request, 'backend/team.html', {'menu': menu, 'title': 'Наша команда'})


def shedule(request):
    return render(request, 'backend/shedule.html', {'menu': menu, 'title': 'Расписание'})
