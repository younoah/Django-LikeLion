from django import forms
from .models import FuncBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = FuncBlog
        fields = ['title', 'body']