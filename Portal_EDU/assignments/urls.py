from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^assignment/', 'assignments.views.create_assignment', name='create_assignment'),

)
