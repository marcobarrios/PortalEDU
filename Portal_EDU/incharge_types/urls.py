from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'incharge_types.views.create_incharge_type', name='create_incharge_type'),

)