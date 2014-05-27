from django.db import models


class Competitor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="static")
    description = models.TextField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    drawn = models.IntegerField()
    born_date = models.DateTimeField(auto_created=True)
    publication_date = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __unicode__(self):
        return self.first_name+' '+self.last_name