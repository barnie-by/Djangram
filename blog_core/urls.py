from django.urls import path
from .views import Home, PostDetail, Add

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('article/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('article/<int:pk>-<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('add_post/', Add.as_view(), name='post_add')
]
