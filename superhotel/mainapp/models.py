from django.db import models

# Create your models here.

class Table(models.Model):
	field = models.CharField( max_length=100)