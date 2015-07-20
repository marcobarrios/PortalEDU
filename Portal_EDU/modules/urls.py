from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'modules.views.create_module', name='create_module'),
    url(r'^$', 'modules.views.view_all_modules', name='view_all_modules'),
    url(r'^(?P<pk>[0-9]+)/', 'modules.views.view_module', name='view_module'),  

)