from django.db import models

# Create your models here.
class credentials(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length= 13)
    address = models.TextField()
    date = models.DateField()