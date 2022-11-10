from django.contrib import admin
from post.models import PostNotice, PostActivity, PostNews, PostOutstanding


admin.site.register(PostNotice)
admin.site.register(PostActivity)
admin.site.register(PostNews)
admin.site.register(PostOutstanding)


