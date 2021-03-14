from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_author = models.CharField(max_length=60)
    blog_title = models.CharField(max_length=60)
    blog_description = models.CharField(max_length=250)
    blog_pub_date = models.DateTimeField()
    blog_image = models.ImageField(upload_to='images/blog_images/', blank=True)

    def __str__(self):
        blog_by = self.blog_title + ' by ' + self.blog_author
        return blog_by
