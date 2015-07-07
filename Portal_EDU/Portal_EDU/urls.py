from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Portal_EDU.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^crear/', 'schools.views.crear', name='crear'),
    url(r'^', include('academic_calendars.urls')),
    url(r'^', include('assignments.urls')),
    url(r'^', include('blood_types.urls')),
    url(r'^', include('classrooms.urls')),
    url(r'^', include('contact_types.urls')),
    url(r'^', include('contacts.urls')),
    url(r'^', include('courses.urls')),
    url(r'^', include('schools.urls')),


)
