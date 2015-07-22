from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_entrance_schedules.views.create_staff_entrance_schedule', name='create_staff_entrance_schedule'),
    url(r'^', 'staff_entrance_schedules.views.view_all_staff_entrance_schedules', name='view_all_staff_entrance_schedules'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_entrance_schedules.views.view_staff_entrance_schedule', name='view_staff_entrance_schedule'),

)