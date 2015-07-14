from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^section/', 'sections.views.create_section', name='create_section'),

)