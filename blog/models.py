
#coding=utf-8
from datetime import timedelta
from django.db import models
from django.contrib import admin

# Create your models here.
from django.utils import timezone
from django.utils.datetime_safe import datetime


class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #时间格式有问题明天再看下
    # def was_published_recently(self):
    #     try:
    #
    #         # type(datetime.day(days=1))
    #         type(self.pub_date)
    #         return self.pub_date >= timezone.now()
    #     except Exception , e:
    #         return e
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now


    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
