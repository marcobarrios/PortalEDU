from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'notes.views.create_note', name='create_note'),

)