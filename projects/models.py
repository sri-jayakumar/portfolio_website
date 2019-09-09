from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    categroy = models.CharField(max_length=100)
    calendar = models.DateField()

    def __str__(self):
        return self.title