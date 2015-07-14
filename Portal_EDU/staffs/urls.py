from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^staff/', 'staffs.views.create_staff', name='create_staff'),

)
