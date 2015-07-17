from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'entrance_schedules.views.create_entrance_schedule', name='create_entrance_schedules'),
    url(r'^$', 'entrance_schedules.views.view_all_entrance_schedules', name='view_all_entrance_schedules'),
    url(r'^(?P<pk>[0-9]+)/', 'entrance_schedules.views.view_entrance_schedule', name='view_entrance_schedule'),  
)