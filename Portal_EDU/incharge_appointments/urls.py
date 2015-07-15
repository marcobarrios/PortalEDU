from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'incharge_appointments.views.create_incharge_appointment', name='create_incharge_appointment'),

)