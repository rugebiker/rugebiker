from django.conf.urls import patterns, include, url
from blog.feed import BlogFeed

urlpatterns = patterns('',
    url(r'^feed/$', BlogFeed()),
)

urlpatterns += patterns('blog.views',
    # Examples:
    # url(r'^$', 'rugebiker.views.home', name='home'),
    url(r'^$', "main"),
    url(r'^archive/$', "archive"),
    url(r'^(?P<post_url>[\w\_&-]+)/$', "post_page"),
    url(r'^tag/(?P<tag>[\w\_&-]+)/$', "tag"),
)
