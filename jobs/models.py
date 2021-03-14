from django.db import models

from django.utils import timezone

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    # default=timezone.now()
    job_pub_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
