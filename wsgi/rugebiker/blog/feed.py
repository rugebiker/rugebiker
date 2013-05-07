# -*- coding: utf-8 -*- 
from django.contrib.syndication.views import Feed
from blog.models import Post 
from django.http import Http404

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

class TagFeed(Feed):

    title = "Biker"
    description = "De linux, el universo y todo lo demás!"
    link = "/linux/feed/"

    def get_object(self, request, tag):
        try:
            item = Post.objects.filter(tags__name__exact=tag)
            if item:
                item.tag = tag
                return item
            else:
                raise Http404
        except:
            raise Http404
        #return get_object_or_404(Post, tags__name=tag)

    def items(self, item):
        return Post.objects.filter(tags__name__exact=item.tag).order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body 

    def item_link(self, item):
        return u"/blog/%s" % item.post_url

    def author_name(self, item):
        return "biker"
