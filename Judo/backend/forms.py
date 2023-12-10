from django import forms
from .models import *
from django.forms import ModelForm


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'slug', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PostsPhoto
        fields = ['photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (['body'])


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'no-label', 'placeholder': 'Ваше имя'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'no-label', 'placeholder': 'Ваш Email'}
        )
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'no-label', 'placeholder': 'Ваш телефон'}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'no-label', 'placeholder': 'Сообщение'}
        )
    )




