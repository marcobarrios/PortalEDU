from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'student_reports.views.create_student_report', name='create_student_report'),

)
