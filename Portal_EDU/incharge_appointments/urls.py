from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'incharge_appointments.views.create_incharge_appointment', name='create_incharge_appointment'),
    url(r'^$', 'incharge_appointments.views.view_all_incharge_appointments', name='view_all_incharge_appointments'),
    url(r'^(?P<pk>[0-9]+)/', 'incharge_appointments.views.view_incharge_appointment', name='view_incharge_appointment'),  

)