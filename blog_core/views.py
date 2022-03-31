from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse

from blog_core.models import Posts, Comments
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostsForm, CommentForm


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

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            post_slug = post.slug
            form.instance.author = request.user
            form.instance.post = post
            form.save()

            return redirect(f'http://127.0.0.1:8000/post/{post_slug}/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        post_comments_count = Comments.objects.all().filter(post=self.object.id).count()
        context.update({
            'post_comments_count': post_comments_count
        })
        return context


class AddPost(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'add_post.html'
    form_class = PostsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
