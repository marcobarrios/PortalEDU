from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'extra_curricular_activities.views.create_extra_curricular_activity', name='create_extra_curricular_activity'),

)