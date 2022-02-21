from django.contrib import admin

from .models import Comments
from .models import Posts
from .models import Likes
from .models import Media


admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Media)

