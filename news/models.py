from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    account = models.ForeignKey(User)
    publication_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=1024)
    account = models.ForeignKey(User)
    publication_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.title