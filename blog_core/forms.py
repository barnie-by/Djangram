from .models import Posts
from django.forms import ModelForm, Textarea


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['author', 'content']

        widgets = {
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'maxlength': 50,
            })
        }
