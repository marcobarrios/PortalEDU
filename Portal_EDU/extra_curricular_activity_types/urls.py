from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-extracurricularactivitytype/', 'extra_curricular_activity_types.views.create_extracurricularactivitytype', name='create_extracurricularactivitytype'),

)