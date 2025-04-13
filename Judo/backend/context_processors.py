from .models import File

menu = [
        {'title': "Новости", 'url_name': 'backend:post_list'},
        {'title': "Расписание", 'url_name': 'backend:shedule'},
        {'title': "Фотогалерея", 'url_name': 'backend:gallery'},
        {'title': "Стоимость", 'url_name': 'backend:team'},
        {'title': "О клубе", 'url_name': 'backend:team'},
        ]


def global_context(request):
    files = File.objects.all()
    return {
        'files': files,
        'menu': menu,
    }
