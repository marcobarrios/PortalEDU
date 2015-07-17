from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'grades.views.create_grade', name='create_grade'),
    url(r'^$', 'grades.views.view_all_grades', name='view_all_grades'),
    url(r'^(?P<pk>[0-9]+)/', 'grades.views.view_grade', name='view_grade'),  

)