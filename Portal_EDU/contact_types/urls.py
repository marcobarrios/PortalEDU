from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'contact_types.views.create_contact_type', name='create_contact_type'),

)
