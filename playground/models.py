from django.db import models

# Create your models here.
# I am creating "Playground"  table by creating a Playground class
class Playground(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
