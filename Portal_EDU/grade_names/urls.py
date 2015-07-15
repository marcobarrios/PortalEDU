from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'grade_names.views.create_grade_name', name='create_grade_name'),

)