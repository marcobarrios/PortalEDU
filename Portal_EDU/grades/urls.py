from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'grades.views.create_grade', name='create_grade'),

)