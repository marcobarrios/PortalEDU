from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'contact_types.views.create_contact_type', name='create_contact_type'),
    url(r'^$', 'contact_types.views.view_all_contact_types', name='view_all_contact_types'),
    url(r'^(?P<pk>[0-9]+)/', 'contact_types.views.view_contact_type', name='view_contact_type'),  

)
