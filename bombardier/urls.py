from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'news.views.news', name='news'),
    url(r'^news$', 'news.views.news', name='news'),
    url(r'^zawodnicy$', 'news.views.news', name='news'),
    url(r'^terminy$', 'news.views.news', name='news'),
    url(r'^galeria', 'news.views.news', name='news'),
    url(r'^kontakt$', 'news.views.news', name='news'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    url(r'^admin/', include(admin.site.urls)),
)
