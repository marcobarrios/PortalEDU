from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^student-control-list/', 'student_control_list.views.create_student_control_list', name='create_student_control_list'),

)
