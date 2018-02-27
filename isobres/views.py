# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.

def homepage(request):
        template = get_template("homepage.html")
        variables = {
            "version" : "1.0.0.01"
        }
        output = template.render(variables)

        return HttpResponse(output)
