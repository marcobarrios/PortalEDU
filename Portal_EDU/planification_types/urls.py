from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^planification-type/', 'planification_types.views.create_planification_type', name='create_planification_type'),

)