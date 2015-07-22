from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staff_types.views.create_staff_type', name='create_staff-type'),
    url(r'^', 'staff_types.views.view_all_staff_types', name='view_all_staff_types'),
    url(r'^(?P<pk>[0-9]+)/', 'staff_types.views.view_staff_type', name='view_staff_type'),

)
