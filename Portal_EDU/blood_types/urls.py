from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'blood_types.views.create_blood_type', name='create_blood_type'),
    url(r'^$', 'blood_types.views.view_all_blood_types', name='view_all_blood_types'),
    url(r'^(?P<pk>[0-9]+)/', 'blood_types.views.view_blood_type', name='view_blood_type'),

)
