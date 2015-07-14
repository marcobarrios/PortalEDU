from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^staff-type/', 'staff_types.views.create_staff_type', name='create_staff-type'),

)
