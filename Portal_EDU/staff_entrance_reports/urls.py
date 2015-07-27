from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_entrance_reports.views.create_staff_entrance_report', name='create_staff_entrance_report'),
    url(r'^', 'staff_entrance_reports.views.view_all_staff_entrance_reports', name='view_all_staff_entrance_reports'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_entrance_reports.views.view_staff_entrance_report', name='view_staff_entrance_report'),

)
