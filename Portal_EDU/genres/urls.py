from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'genres.views.create_genre', name='create_genre'),

)
