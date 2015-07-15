from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_activities.views.create_staff_activity', name='create_staff_activity'),

)
