from blog_core.models import Posts
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostsForm


class Home(ListView):
    paginate_by = 5
    model = Posts
    template_name = 'all_posts.html'
    context_object_name = "post"
    ordering = ['-published']


class PostDetail(DetailView):
    model = Posts
    query_pk_and_slug = True
    template_name = 'post_detail.html'


class AddPost(CreateView):
    model = Posts
    template_name = 'add_post.html'
    form_class = PostsForm
    # fields = ('author', 'content')
