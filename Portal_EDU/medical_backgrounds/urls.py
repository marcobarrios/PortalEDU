from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^medical-background/', 'medical_backgrounds.views.create_medical_background', name='create_medical_background'),

)