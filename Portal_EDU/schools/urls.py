from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-school/', 'schools.views.create_school', name='create_school'),

)
