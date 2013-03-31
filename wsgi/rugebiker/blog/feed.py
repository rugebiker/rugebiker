# -*- coding: utf-8 -*- 
from django.contrib.syndication.views import Feed
from blog.models import Post 

class BlogFeed(Feed):
    
    title = "Biker"
    description = "De linux, el universo y todo lo demás!"
    link = "/feed/"
    
    def items(self):
        return Post.objects.all().order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body 

    def item_link(self, item):
        return u"/blog/%s" % item.post_url

    def author_name(self, item):
        return "biker"

class LinuxFeed(Feed):

    title = "Biker"
    description = "De linux, el universo y todo lo demás!"
    link = "/linux/feed/"

    def items(self):
        return Post.objects.get(tags__contains='linux').order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body 

    def item_link(self, item):
        return u"/blog/%s" % item.post_url

    def author_name(self, item):
        return "biker"
