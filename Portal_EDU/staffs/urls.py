from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staffs.views.create_staff', name='create_staff'),

)
