from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'extra_curricular_activities.views.create_extra_curricular_activity', name='create_extra_curricular_activity'),
    url(r'^$', 'extra_curricular_activities.views.view_all_extra_curricular_activities', name='view_all_extra_curricular_activities'),
    url(r'^(?P<pk>[0-9]+)/', 'extra_curricular_activities.views.view_extra_curricular_activity', name='view_extra_curricular_activity'),  

)