from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'assignments.views.create_assignment', name='create_assignment'),
    url(r'^$', 'assignments.views.view_all_assignments', name='view_all_assignments'),
    url(r'^(?P<pk>[0-9]+)/', 'assignments.views.view_assignment', name='view_assignment'),

)
