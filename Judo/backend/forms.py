from django import forms
from .models import *


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