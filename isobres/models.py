# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor (models.Model):
    name = models.CharField(max_length=80)

    def __unicode(self):
        return self.name


class Bribe(models.Model):
    """ """
    amount = models.IntegerField()
    concept = models.TextField(max_length=150)
    date = models.DateTimeField()
    donor = models.ForeignKey(Donor)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.concept[:60]+"-"+str(self.amount)+"€"
