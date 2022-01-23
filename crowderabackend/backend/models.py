from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=20)
    duration=models.IntegerField()
    id=models.AutoField(primary_key=True)
    image=models.URLField()

    def __str__(self):
        self.name

class Cast(models.Model):
    castName=models.CharField(max_length=20)
    des=models.TextField()
    
