from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordResetForm
from .models import Movie, Review, Comment

User = get_user_model()

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'date_released',
            'rating',
            'poster',
        )

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'author',
            'details',
        )

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'review',
            'author',
            'comment',
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

