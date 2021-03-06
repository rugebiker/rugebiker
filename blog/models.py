from django.db import models
from taggit.managers import TaggableManager
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager(blank=True)
    post_url = models.CharField(max_length=30, unique=True)
    lang = models.CharField(max_length=2)

    def __unicode__(self):
        return self.title


class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
