from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'poll_home'}),
    url(r'^join/$', views.join, name='registration'),
)