from django.urls import path
from .views import Home, PostDetail, AddPost, likes_handler

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view(), name='post_add'),
    path('like/post/<str:slug>/', likes_handler, name='post_likes')
]
