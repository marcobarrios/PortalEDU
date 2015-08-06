from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'staffs.views.create_staff', name='create_staff'),
    url(r'^PortalTeacher/', 'staffs.views.portal_teacher', name='portal_teacher'),
    url(r'^PortalAdministrative/', 'staffs.views.portal_administrative', name='portal_administrative'),

)
