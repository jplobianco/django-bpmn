# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    some_data = 'some data'
    context = {'some_data': some_data}
    template = 'core/index.html'
    return render(request, template, context)
