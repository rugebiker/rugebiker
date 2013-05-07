from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rugebiker.views.home', name='home'),
    # url(r'^rugebiker/', include('rugebiker.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name="info.html")),
    url(r'^es/$', TemplateView.as_view(template_name="info.html"),{'lang':'es'}),
    url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
