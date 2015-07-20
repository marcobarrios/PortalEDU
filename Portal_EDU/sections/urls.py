from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'sections.views.create_section', name='create_section'),
    url(r'^$', 'sections.views.view_all_sections', name='view_all_sections'),
    url(r'^(?P<pk>[0-9]+)/', 'sections.views.view_section', name='view_section'),  


)