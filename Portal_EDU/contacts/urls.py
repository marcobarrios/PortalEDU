from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^contact/', 'contacts.views.create_contact', name='create_contact'),

)
