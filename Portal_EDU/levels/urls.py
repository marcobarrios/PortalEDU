from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'levels.views.create_level', name='create_level'),

)