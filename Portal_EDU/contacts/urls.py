from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^create-contact/', 'contacts.views.create_contact', name='create_contact'),

)
