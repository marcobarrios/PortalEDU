from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^staff-appointment/', 'staff_appointments.views.create_staff_appointment', name='create_staff_appointment'),

)
