#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from blog import views
from blog.views import AboutView

urlpatterns = patterns('',

    # url(r'^index/$', 'blog.views.index'),
     # ex: /MyBlog/
    # url(r'^$', views.index, name='index'),

    url(r'^polls/', include('polls.urls', namespace="polls",app_name='polls')),
    # ex: /MyBlog/5/
    url(r'^admin/', include(admin.site.urls)),
   url(r'^about/', AboutView.as_view()),
    # ex: /MyBlog/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

)