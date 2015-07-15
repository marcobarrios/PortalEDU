from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'planifications.views.create_planification', name='create_planification'),

)