from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'courses.views.create_course', name='create_course'),

)