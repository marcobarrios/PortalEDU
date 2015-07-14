from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^extra-curricular-activity-type/', 'extra_curricular_activity_types.views.create_extracurricularactivitytype', name='create_extracurricularactivitytype'),

)