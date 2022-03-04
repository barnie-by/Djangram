from blog_core.models import Posts
from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Posts
    template_name = 'all_posts.html'
    context_object_name = "post"


class PostDetail(DetailView):
    model = Posts
    template_name = 'post_detail.html'
