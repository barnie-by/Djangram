from .models import Posts, Comments
from django.forms import ModelForm, Textarea, TextInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'post_image']
        widgets = {
            'content': Textarea(attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; width: 100%;',
                'class': 'form-control',
                'placeholder': 'Add some text...',
                'maxlength': 550,
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

        widgets = {
            'content': TextInput(attrs={
                'style': 'border: 1.25px solid darkgray; border-radius: 10px; height: 35px; width: 100%; align:center',
                'placeholder': 'Add comment...',

            })
        }
