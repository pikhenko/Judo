from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.views.generic import TemplateView

from . import views
from .views import EmailVerify, profile


app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'),
         name='logout'),
    path('signup/', views.SignUp.as_view(),
         name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),

    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='users/invalid_verify.html'),
        name='invalid_verify'
    ),

    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),

    path(
        'confirm_email/',
        TemplateView.as_view(template_name='users/confirm_email.html'),
        name='confirm_email'
    ),


    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html'),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'),
        name='password_change_done'
    ),
    path('password_reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset_form.html'),
         name='password_reset_form'
         ),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('profile/', profile, name='users-profile'),
]
