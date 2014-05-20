from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    creation_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.name
