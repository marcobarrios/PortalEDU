from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'assignments.views.create_assignment', name='create_assignment'),

)
