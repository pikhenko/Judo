from django.urls import path


from .views import index, team, photo, shedule, about, add_page, login, post_list, read_post
app_name = 'backend'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('post_list/', post_list, name='post_list'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', read_post, name='read_post'),
    path('add_page/', add_page, name='add_page'),
]
