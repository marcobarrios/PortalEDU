from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^staff-meeting-schedule/', 'staff_meeting_schedules.views.create_staff_meeting_schedule', name='create_staff_meeting_schedule'),

)
