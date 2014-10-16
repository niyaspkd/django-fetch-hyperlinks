from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home', 'bss.views.home'),
    url(r'^he', 'bss.views.he'),
  
   

    
)
