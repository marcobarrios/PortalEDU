from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'planification_types.views.create_planification_type', name='create_planification_type'),
    url(r'^$', 'planification_types.views.view_all_planification_types', name='view_all_planification_types'),
    url(r'^(?P<pk>[0-9]+)/', 'planification_types.views.view_planification_type', name='view_planification_type'),  

)