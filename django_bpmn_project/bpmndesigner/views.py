# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def modeler(request):

    bpmn_filename = 'https://cdn.rawgit.com/bpmn-io/bpmn-js-examples/dfceecba/starter/diagram.bpmn'
    context = {'bpmn_filename': bpmn_filename}
    template = 'bpmndesigner/modeler.html'
    return render(request, template, context)    


