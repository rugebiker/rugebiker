from django.conf.urls import patterns, include, url
from blog.feed import BlogFeed, TagFeed

urlpatterns = patterns('',
    url(r'^feed/$', BlogFeed()),
    url(r'^(?P<tag>[\w\_&-]+)/feed/$', TagFeed()),
)

urlpatterns += patterns('blog.views',
    url(r'^$', "main", {'lang': 'en'}),
    url(r'^es/$', "main", {'lang': 'es'}),
    url(r'^log/$', "log", {'lang': 'en'}),
    url(r'^log/es/$', "log", {'lang': 'es'}),
    url(r'^(?P<post_url>[\w\_&-]+)/$', "post_page"),
    url(r'^tag/(?P<tag>[\w\_&-]+)/$', "tag", {'lang': 'en'}),
    url(r'^tag/(?P<tag>[\w\_&-]+)/es/$', "tag", {'lang': 'es'}),
)
