from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'mainapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^(?P<ref_id>.*)$',
                           'mainapp.views.profile', name='profile'),


                       )
