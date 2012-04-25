from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)