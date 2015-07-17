from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'courses.views.create_course', name='create_course'),
    url(r'^$', 'courses.views.view_all_courses', name='view_all_courses'),
    url(r'^(?P<pk>[0-9]+)/', 'courses.views.view_course', name='view_course'),  


)