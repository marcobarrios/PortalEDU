from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'planifications.views.create_planification', name='create_planification'),
    url(r'^$', 'planifications.views.view_all_planifications', name='view_all_planifications'),
    url(r'^(?P<pk>[0-9]+)/', 'planifications.views.view_planification', name='view_planification'),  

)