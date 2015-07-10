from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'students.views.new_student', name='new_student'),
)
