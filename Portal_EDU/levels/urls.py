from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'levels.views.create_level', name='create_level'),
    url(r'^$', 'levels.views.view_all_levels', name='view_all_levels'),
    url(r'^(?P<pk>[0-9]+)/', 'levels.views.view_level', name='view_level'),  

)