from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_entrance_reports.views.create_staff_entrance_report', name='create_staff_entrance_report'),

)
