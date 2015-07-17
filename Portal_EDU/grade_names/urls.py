from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'grade_names.views.create_grade_name', name='create_grade_name'),
    url(r'^$', 'grade_names.views.view_all_grade_names', name='view_all_grade_names'),
    url(r'^(?P<pk>[0-9]+)/', 'grade_names.views.view_grade_name', name='view_grade_name'),  

)