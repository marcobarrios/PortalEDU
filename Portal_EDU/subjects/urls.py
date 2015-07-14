from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^subject/', 'subjects.views.create_subject', name='create_subject'),

)
