from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Staff(models.Model):
    staffID     =   models.IntegerField()
    staffname   =   models.CharField(max_length=50)
    staffemail  =   models.EmailField(max_length=70)
    