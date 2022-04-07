from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from blog_core.models import Posts, Comments, Likes
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostsForm, CommentForm


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

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            post_slug = post.slug
            form.instance.author = request.user
            form.instance.post = post
            form.save()

            return redirect('post_detail', slug=post_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        post_comments_count = Comments.objects.all().filter(post=self.object.id).count()
        post_likes_count = Likes.objects.filter(liked_post_id=self.object.id).count()
        context.update({
            'post_comments_count': post_comments_count,
            'post_likes_count': post_likes_count
        })
        return context


class AddPost(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'add_post.html'
    form_class = PostsForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def likes_handler(request, slug):
    user_object = request.user
    post_object = get_object_or_404(Posts, slug=slug)
    like_item, created = Likes.objects.get_or_create(
        liked_post=post_object,
        user_id=user_object
    )
    if created is False:
        like_item.delete()

    return redirect('post_detail', slug=slug)
