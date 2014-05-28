from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'news.views.show', name='news'),
    url(r'^news$', 'news.views.show', name='news'),
    url(r'^zawodnicy$', 'competitors.views.show', name='competitors'),
    url(r'^terminy$', TemplateView.as_view(template_name='timetable/timetable.html'), name="timetable"),
    url(r'^galeria', 'news.views.show', name='news'),
    url(r'^kontakt$', 'contact.views.contact', name='news'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
