from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from conf.urls import include
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'money.views.display_image'), #Look for the root webpage
                       url(r'^admin/', include(admin.site.urls)),
                       )
