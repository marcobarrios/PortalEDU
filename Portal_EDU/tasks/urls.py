from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'tasks.views.create_task', name='create_task'),

)
