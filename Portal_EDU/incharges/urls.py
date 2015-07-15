from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'incharges.views.create_incharge', name='create_incharge'),

)