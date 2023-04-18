from django.urls import path

from .views import index, team, photo, shedule

urlpatterns = [
<<<<<<< HEAD
    path('', index, name='index'),
    path('team/', team),
    path('photo/', photo),
    path('shedule/', shedule),
]
=======
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('add_page/', add_page, name='add_page'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', read_post, name='post')
]
>>>>>>> ea669110db9a284137eb5eb840921232f54e0809
