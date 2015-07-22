from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_meeting_schedules.views.create_staff_meeting_schedule', name='create_staff_meeting_schedule'),
    url(r'^', 'staff_meeting_schedules.views.view_all_staff_meeting_schedules', name='view_all_staff_meeting_schedules'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_meeting_schedules.views.view_staff_meeting_schedule', name='view_staff_meeting_schedule'),

)
