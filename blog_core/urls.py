from django.urls import path
from .views import Home, PostDetail, AddPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view(), name='post_add')
]
