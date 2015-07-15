from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'modules.views.create_module', name='create_module'),

)