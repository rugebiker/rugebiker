from django.contrib import admin
from django_browserid.admin import site as browserid_admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.unregister(Post)
browserid_admin.register(Post, PostAdmin)
