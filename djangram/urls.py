from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog_core.urls')),
    path('admin/', admin.site.urls),
    path('authentication/', include('django.contrib.auth.urls')),
    path('authentication/', include('authentication.urls'))

]
