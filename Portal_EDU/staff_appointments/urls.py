from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_appointments.views.create_staff_appointment', name='create_staff_appointment'),
    url(r'^$', 'staff_appointments.views.view_all_staff_staff_appointments', name='view_all_staff_appointments'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_appointments.views.view_staff_appointment', name='view_staff_appointment'),

)

