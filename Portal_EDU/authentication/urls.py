from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^ingresar/', 'authentication.views.apolodb_login', name='apolodb_login'),

)
