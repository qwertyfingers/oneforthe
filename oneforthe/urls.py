from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from conf.urls import include
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^test_site/$', 'money.views.display_image'), #Look for test_site
                       url(r'^admin/', include(admin.site.urls)),
                       )
