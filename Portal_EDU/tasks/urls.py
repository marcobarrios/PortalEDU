from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-task/', 'tasks.views.create_task', name='create_task'),

)
