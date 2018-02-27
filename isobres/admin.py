# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bribe
from isobres.models import Donor

# Register your models here.
admin.site.register(Bribe)
admin.site.register(Donor)
