# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Responses(models.Model):
    message=models.CharField(max_length=300)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class ReportedPoor(models.Model):
    name=models.CharField(max_length=300)
    contact=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    cnic=models.CharField(max_length=300)