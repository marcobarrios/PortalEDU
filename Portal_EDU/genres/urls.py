from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^new/', 'genres.views.create_genre', name='create_genre'),
    url(r'^$', 'genres.views.view_all_genres', name='view_all_genres'),
    url(r'^(?P<pk>[0-9]+)/', 'genres.views.view_genre', name='view_genre'),  

)
