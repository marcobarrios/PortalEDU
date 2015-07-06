from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-academic-calendar/', 'academic_calendars.views.create_academic_calendar', name='create_academic_calendar'),

)
