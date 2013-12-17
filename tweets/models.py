from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.name)


class Tweet(models.Model):
    content = models.CharField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return unicode(self.content)
