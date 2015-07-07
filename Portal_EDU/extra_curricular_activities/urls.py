from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-extracurricularactivity/', 'extra_curricular_activities.views.create_extracurricularactivity', name='create_extracurricularactivity'),

)