from django.urls import path

from .views import index, team, photo, shedule, about, add_page, login, read_post

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('post_list/', post_list, name='post_list'),
    path('login/', login, name='login'),
<<<<<<< HEAD
    path('post/<slug:post_slug>/', read_post, name='read_post'),
    path('add_page/', add_page, name='add_page'),
]
=======
    path('post/<int:post_id>/', read_post, name='post')
]
>>>>>>> 80b08dbb6b766f69fd5783439bdc45c52f8b35fe
