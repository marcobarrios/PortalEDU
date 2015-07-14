from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^staff-entrance-schedule/', 'staff_entrance_schedules.views.create_staff_entrance_schedule', name='create_staff_entrance_schedule'),

)