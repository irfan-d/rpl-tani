from django.db import models

# Create your models here.
class Tumbuhan(models.Model):
  gambarTanam = models.ImageField
  namaTanam = models.CharField(max_length=50)
  jenisTanam = models.CharField(max_length=50)
  deskripsiTanam = models.CharField(max_length=250)

  def __str__(self):
    return self.namaTanam