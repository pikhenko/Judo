from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator as \
    token_generator
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from .forms import AuthenticationForm
from .forms import UpdateProfileForm, UpdateUserForm
from backend.views import menu
from backend.models import *
from django.contrib import messages
from .models import Profile

from .utils import send_email_for_verify


from django.urls import reverse_lazy
from django.views.generic import CreateView

User = get_user_model()


def my_login_view(request, *args, **kwargs):
    view = LoginView.as_view(template_name='users/login.html', extra_context={'menu': menu})
    return view(request, *args, **kwargs)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('backend:home')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class SignUp(CreateView):
    template_name = 'users/signup.html'

    def get(self, request):
        context = {
            'menu': menu,
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('users:confirm_email')
        context = {
            'menu': menu,
            'form': form,
        }
        return render(request, self.template_name, context)


@login_required
def profile(request):
    user = request.user
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'users/profile.html', {'menu': menu,
                                                  'user_form': user_form,
                                                  'profile_form': profile_form,})


