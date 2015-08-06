from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'incharges.views.create_incharge', name='create_incharge'),
    url(r'^$', 'incharges.views.view_all_incharges', name='view_all_incharges'),
    url(r'^(?P<pk>[0-9]+)/', 'incharges.views.view_incharge', name='view_incharge'),
    url(r'^PortalIncharges/', 'incharges.views.portal_incharge', name='portal_incharge'), 

)