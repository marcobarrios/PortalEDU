from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'tasks.views.create_task', name='create_task'),
	url(r'^', 'tasks.views.view_all_tasks', name='view_all_tasks'),
    url(r'^(?P<pk>[0-9]+)/', 'tasks.views.view_task', name='view_task'),

)
