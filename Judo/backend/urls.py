from django.urls import path


from .views import index, team, photo, shedule, add_page, login, post_list, read_post, post_comment, gallery, addPhoto, viewPhoto
pp_name = 'backend'

urlpatterns = [
    path('', index, name='home'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('post_list/', post_list, name='post_list'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', read_post, name='read_post'),
    path('add_page/', add_page, name='add_page'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('gallery', gallery, name='gallery'),
    path('photo/<str:pk>/', viewPhoto, name='photo2'),
    path('add/', addPhoto, name='add'),
]
