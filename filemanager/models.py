from django.db import models
from time import time

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class File(models.Model):
    fileName = models.CharField(max_length=200)
    desc = models.TextField()
    pub_date = models.DateTimeField('date published')
    file_to_upload = models.FileField(upload_to = get_upload_file_name)

    def __unicode__(self):
        return self.fileName
