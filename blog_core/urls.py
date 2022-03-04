from django.urls import path
from .views import Home, PostDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article/<int:pk>', PostDetail.as_view(), name='post_detail')

]
