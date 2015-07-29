from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'authentication.views.apolodb_login', name='apolodb_login'),
    url(r'^logout/', 'authentication.views.log_out', name='log_out'),

)