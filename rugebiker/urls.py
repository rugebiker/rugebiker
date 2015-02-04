from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

from django_browserid.admin import site as browserid_admin
browserid_admin.include_password_form = True
browserid_admin.copy_registry(admin.site)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="info.html")),
    url(r'^es/$', TemplateView.as_view(template_name="info.html"), {'lang': 'es'}),
    url(r'places/$', TemplateView.as_view(template_name="places.html")),
    url(r'places/es/$', TemplateView.as_view(template_name="places.html"), {'lang': 'es'}),
    url(r'', include('django_browserid.urls')),
    url(r'^admin/', include(browserid_admin.urls)),
    url(r'^blog/', include('blog.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    url(r'^admin/', include(admin.site.urls)),
)
