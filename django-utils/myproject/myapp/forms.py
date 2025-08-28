from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        help_texts = {
            'title': 'Enter the title of the post.',
            'content': 'Enter the content of the post.',
        }
        error_messages = {
            'title': {
                'max_length': 'This title is too long.',
            },
            'content': {
                'required': 'Content is required.',
            },
        }