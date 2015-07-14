from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^task/', 'tasks.views.create_task', name='create_task'),

)
