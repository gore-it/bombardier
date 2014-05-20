from django.db import models

from accounts.models import Account


class Comment(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField(max_length=1024)
    account = models.ForeignKey(Account)
    publication_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.title