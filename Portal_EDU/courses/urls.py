from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-course/', 'courses.views.create_course', name='create_course'),

)