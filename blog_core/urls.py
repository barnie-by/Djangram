from django.urls import path
from .views import Home, PostDetail, AddPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('article/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/<uuid:uniqueid>', PostDetail.as_view(), name='post'),
    # path('article/<int:pk>-<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view(), name='post_add')
]
