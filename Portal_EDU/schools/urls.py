from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^school/', 'schools.views.create_school', name='create_school'),

)
