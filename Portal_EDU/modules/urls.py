from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^module/', 'modules.views.create_module', name='create_module'),

)