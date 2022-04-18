from django.urls import path
from .views import Home, PostDetail, AddPost, likes_handler, profile_page, ProfilePage

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view(), name='post_add'),
    path('like/post/<str:slug>/', likes_handler, name='post_likes'),
    path('profile/', profile_page, name='user_profile_page'),
    path('profile/<int:id>', ProfilePage.as_view(), name='user_page')
    # path('user_profile/', page_profile, name='user_page')



]
