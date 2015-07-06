from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-bloodtype/', 'blood_types.views.create_blood_type', name='create_blood_type'),

)
