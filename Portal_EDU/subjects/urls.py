from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'subjects.views.create_subject', name='create_subject'),
    url(r'^', 'subjects.views.view_all_subjects', name='view_all_subjects'),
    url(r'^(?P<pk>[0-9]+)/', 'subjects.views.view_subject', name='view_subject'),

)
