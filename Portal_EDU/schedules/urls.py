from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'schedules.views.create_schedule', name='create_schedule'),
    url(r'^$', 'schedules.views.view_all_schedules', name='view_all_schedules'),
    url(r'^(?P<pk>[0-9]+)/', 'schedules.views.view_schedule', name='view_schedule'),  

)