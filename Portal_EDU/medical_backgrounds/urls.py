from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'medical_backgrounds.views.create_medical_background', name='create_medical_background'),
    url(r'^$', 'medical_backgrounds.views.view_all_medical_backgrounds', name='view_all_medical_backgrounds'),
    url(r'^(?P<pk>[0-9]+)/', 'medical_backgrounds.views.view_medical_background', name='view_medical_background'),  

)