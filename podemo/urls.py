from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from organization import views


#admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'podemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^podemo/admin/', include(admin.site.urls)),
    #url(r'^organization/', include('organization.urls', namespace="organization")),
    url(r'^podemo/', include(router.urls)),
    (r'^$', 'django.views.static.serve', {'document_root':'/local/content/ctrp/apps/podemo/','path':'index.html'}),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


