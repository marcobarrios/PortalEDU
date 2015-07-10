from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^planification/', 'planifications.views.create_planification', name='create_planification'),

)