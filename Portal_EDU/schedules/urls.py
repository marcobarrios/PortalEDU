from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^schedule/', 'schedules.views.create_schedule', name='create_schedule'),

)