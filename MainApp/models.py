from django.db import models

# Create your models here.
class File(models.Model):
  file = models.FileField(upload_to="files")

class CandleData(models.Model):
  name = models.CharField(max_length=50)
  date = models.DateField()
  time = models.TimeField()
  open = models.FloatField()
  high = models.FloatField()
  low = models.FloatField()
  close = models.FloatField()
  volume = models.IntegerField()