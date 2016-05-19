from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from blog import views
urlpatterns = patterns('',
                       # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
                       # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
                       #    # ex: /MyBlog/5/results/
                       # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


                   )