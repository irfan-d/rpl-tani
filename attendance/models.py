from django.db import models
from tanaman.models import Tumbuhan
# Create your models here.

class Attendances(models.Model):
  namaTanam = models.ForeignKey(Tumbuhan, on_delete=models.CASCADE)
  waktu = models.DateTimeField("Absen")

  def __str__(self):
    return self.waktu