from django.urls import path

from .views import index, team, photo, shedule, about, add_page, login, read_post
app_name = 'backend'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('add_page/', add_page, name='add_page'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', read_post, name='post')
]
