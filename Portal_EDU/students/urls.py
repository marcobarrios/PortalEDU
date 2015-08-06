from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'students.views.new_student', name='new_student'),url(r'^PortalAdministrative/', 'staffs.views.portal_administrative', name='portal_administrative'),
    url(r'^PortalStudent/', 'students.views.portal_student', name='portal_student'),
)
