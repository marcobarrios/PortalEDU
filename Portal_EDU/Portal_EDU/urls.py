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
    url(r'^', include('authentication.urls')),    
    url(r'^', include('blood_types.urls')),
    url(r'^', include('classrooms.urls')),
    url(r'^', include('contact_types.urls')),
    url(r'^', include('contacts.urls')),
    url(r'^', include('courses.urls')),
    url(r'^', include('entrance_schedules.urls')),
    url(r'^', include('extra_curricular_activities.urls')),
    url(r'^', include('extra_curricular_activity_types.urls')),
    url(r'^', include('genres.urls')),
    url(r'^', include('grade_names.urls')),
    url(r'^', include('grades.urls')),
    url(r'^', include('incharge_appointments.urls')),
    url(r'^', include('incharge_types.urls')),
    url(r'^', include('incharges.urls')),
    url(r'^', include('levels.urls')),
    url(r'^', include('medical_backgrounds.urls')),
    url(r'^', include('modules.urls')),
    url(r'^', include('notes.urls')),
    url(r'^', include('planification_types.urls')),
    url(r'^', include('planifications.urls')),
    url(r'^', include('schools.urls')),
    url(r'^', include('schedules.urls')),
    url(r'^', include('tasks.urls')),    
    
)
