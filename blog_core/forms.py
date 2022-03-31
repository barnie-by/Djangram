from .models import Posts, Comments
from django.forms import ModelForm, Textarea, TextInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']

        widgets = {
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'maxlength': 50,
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

        widgets = {
            'content': TextInput(attrs={
                # 'class': 'md-textarea form-control',
                'placeholder': 'Введите комментарий',

            })
        }

