from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'new/', 'schools.views.create_school', name='create_school'),
    url(r'^$', 'schools.views.view_all_schools', name='view_all_schools'),
    url(r'^(?P<pk>[0-9]+)/', 'schools.views.view_school', name='view_school'),  

)
