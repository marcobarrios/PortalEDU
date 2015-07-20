from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_activities.views.create_staff_activity', name='create_staff_activity'),
    url(r'^$', 'staff_activities.views.view_all_staff_activities', name='view_all_staff_activities'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_activities.views.view_staff_activity', name='view_staff_activity'),  

)
