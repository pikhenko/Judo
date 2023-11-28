from django.urls import path


from .views import (index, team, photo, shedule, add_page, login,
                    post_list, read_post, post_comment, gallery,
                    add_photo, view_photo, delete_photo, contact)
app_name = 'backend'

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
    path('delete_photo/<str:pk>/', delete_photo, name='delete_photo'),
    path('photo/<str:pk>/', view_photo, name='view_photo'),
    path('add/', add_photo, name='add'),
    path('contact/', contact, name='contact'),
]
