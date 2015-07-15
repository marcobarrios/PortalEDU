from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'entrance_schedules.views.create_entrance_schedule', name='create_entrance_schedules'),

)