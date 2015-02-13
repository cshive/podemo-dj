from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'podemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', 'django.views.static.serve', {'document_root':'/var/djapps/podemo/','path':'index.html'}),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^organization/', include('organization.urls', namespace="organization")),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


