from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'classrooms.views.create_class_room', name='create_class_room'), 
    url(r'^$', 'classrooms.views.view_all_classrooms', name='view_all_classrooms'),
    url(r'^(?P<pk>[0-9]+)/', 'classrooms.views.view_classroom', name='view_classroom'),  

)
