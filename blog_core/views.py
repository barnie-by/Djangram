from blog_core.models import Posts
from django.views.generic import ListView, DetailView, CreateView


class Home(ListView):
    paginate_by = 3
    model = Posts
    template_name = 'all_posts.html'
    context_object_name = "post"
    ordering = ['-published']


class PostDetail(DetailView):
    model = Posts
    query_pk_and_slug = True
    template_name = 'post_detail.html'


class Add(CreateView):
    model = Posts
    template_name = 'add_post.html'
    fields = ('author', 'content')
