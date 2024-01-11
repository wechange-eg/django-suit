from django.urls import patterns, include, path
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples for custom menu
    path('foo/bar/', include(admin.site.urls)),
)
