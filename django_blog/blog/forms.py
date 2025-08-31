from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget
from .models import Post, Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='')

    class Meta:
        model = Comment
        fields = ['content']
