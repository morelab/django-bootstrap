from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'markup_app.views.index', name = 'index'),

    url(r'^typography/blockquotes/$', 'markup_app.views.blockquotes', name = 'blockquotes'),
    url(r'^typography/emphasis/$', 'markup_app.views.emphasis', name = 'emphasis'),
    url(r'^typography/headings/$', 'markup_app.views.headings', name = 'headings'),
    url(r'^typography/lists/$', 'markup_app.views.lists', name = 'lists'),
)

urlpatterns += staticfiles_urlpatterns()
