from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=20)
    duration=models.IntegerField()
    id=models.AutoField(primary_key=True)

    def __str__(self):
        self.name
    