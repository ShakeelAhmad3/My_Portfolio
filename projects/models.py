from django.db import models

# Create your models here.
class projects(models.Model):

    title = models.CharField(max_length= 250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/')
    summary = models.CharField(max_length=250)
    bub_date = models.DateField()

    def __str__(self):
        return self.title