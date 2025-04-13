from django.urls import path

from .views import (index, team, photo, shedule, add_page, login,
                    post_list, read_post, post_comment, gallery, gallery_edit,
                    add_photo, view_photo, delete_photo, download_file,
                    delete_category, news, add_news, price)
app_name = 'backend'

urlpatterns = [
    path('', index, name='home'),
    path('team/', team, name='team'),
    path('photo/', photo, name='photo'),
    path('shedule/', shedule, name='shedule'),
    path('price/', price, name='price'),
    path('post_list/', post_list, name='post_list'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', read_post, name='read_post'),
    path('add_page/', add_page, name='add_page'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),
    path('gallery', gallery, name='gallery'),
    path('gallery_edit', gallery_edit, name='gallery_edit'),
    path('delete_photo/<str:pk>/', delete_photo, name='delete_photo'),
    path('photo/<str:pk>/', view_photo, name='view_photo'),
    path('add/', add_photo, name='add'),
    path('news/', news, name='news'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('category/<int:pk>/', delete_category, name='delete_category'),
    path('add_news/', add_news, name='add_news'),
]
