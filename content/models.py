# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ShExpJob(models.Model):
    career = models.CharField(max_length = 50)
    imgcov = models.FileField(upload_to='ShExp/Job/Cov')
    biref = models.TextField()
    trend = models.TextField()
    category = models.TextField()
    department = models.TextField()
    iceberg = models.FileField(upload_to='ShExp/Job/Ice')
    basicskill = models.TextField()
    coop = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return str(self.career)

class ShExpMan(models.Model):
    career_tag = models.ForeignKey("ShExpJob")
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    imgdis = models.FileField(upload_to='ShExp/Man/Dis')
    imgcov = models.FileField(upload_to='ShExp/Man/Cov')
    intro = models.TextField()
    t3 = models.TextField()
    trend = models.TextField()
    turnback = models.TextField()
    know10 = models.TextField()
    share = models.TextField()
    lifestyle = models.TextField()
    job5 = models.TextField()
    pro4 = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

