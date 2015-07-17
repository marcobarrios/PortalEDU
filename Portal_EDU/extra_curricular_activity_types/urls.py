from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'extra_curricular_activity_types.views.create_extracurricularactivitytype', name='create_extracurricularactivitytype'),
    url(r'^$', 'extra_curricular_activity_types.views.view_all_extra_curricular_activity_types', name='view_all_extra_curricular_activity_types'),
    url(r'^(?P<pk>[0-9]+)/', 'extra_curricular_activity_types.views.view_extra_curricular_activity_type', name='view_extra_curricular_activity_type'),  

)