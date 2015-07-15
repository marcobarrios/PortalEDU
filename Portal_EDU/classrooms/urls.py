from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'classrooms.views.create_class_room', name='create_class_room'),   

)
