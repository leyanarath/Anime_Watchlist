from django.db import models
#
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    def __str__(self):
        return self.name
class mlist(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    mdesc = models.TextField()
    img=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name