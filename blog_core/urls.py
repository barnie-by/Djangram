from django.urls import path
from .views import Home, PostDetail, AddPost, likes_handler, my_profile_page, users_profile_page

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view(), name='post_add'),
    path('like/post/<str:slug>/', likes_handler, name='post_likes'),
    path('profile/', my_profile_page, name='user_profile_page'),
    # path('profile/<int:id>', ProfilePage.as_view(), name='user_page')
    path('user_profile/<int:author_id>', users_profile_page, name='user_page')



]
