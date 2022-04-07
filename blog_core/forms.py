from .models import Posts, Comments
from django.forms import ModelForm, Textarea, TextInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']

        widgets = {
            'content': Textarea(attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; width: 100%',
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
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 100%; align:center',
                'placeholder': 'Добавьте комментарий...',

            })
        }
