from django.db import models

# Create your models here.

class File(models.Model):
    fileName = models.CharField(max_length=200)
    desc = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.fileName
