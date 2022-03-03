from django.shortcuts import render
from blog_core.models import Posts
from django.views.generic import ListView, DetailView


# def base(request):
#     pos = Posts.objects.all()
#     context = {'pos': pos}
#     return render(request, 'base.html', context)
#

class Home(ListView):
    model = Posts
    template_name = 'base.html'
    context_object_name = "post"


class PostDetail(DetailView):
    model = Posts
    template_name = 'post_detail.html'
