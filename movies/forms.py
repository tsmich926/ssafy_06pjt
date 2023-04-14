from django import forms
from .models import Movies,Comment

class MoviesForm(forms.ModelForm):

    class Meta:
        model = Movies
        exclude = (
            'user',
            'like_users',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            'user',
            'movie',)
