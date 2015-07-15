from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'sections.views.create_section', name='create_section'),

)