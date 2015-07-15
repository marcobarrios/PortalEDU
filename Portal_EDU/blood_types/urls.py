from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'blood_types.views.create_blood_type', name='create_blood_type'),

)
