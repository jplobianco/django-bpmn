# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.http import HttpResponse

from django.conf import settings

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import requests 

from urllib2 import Request, urlopen

from xml.dom import minidom

from .models import Diagram
from .forms import ModelerForm

# Create your views here.

def example_diagram():
    diagram = (
    '''
    <?xml version="1.0" encoding="UTF-8"?>
    <bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" id="Definitions_1cm2jxp" targetNamespace="http://bpmn.io/schema/bpmn">
    <bpmn:process id="Process_1" isExecutable="false">
        <bpmn:startEvent id="StartEvent_1" />
    </bpmn:process>
    <bpmndi:BPMNDiagram id="BPMNDiagram_1">
        <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_1">
        <bpmndi:BPMNShape id="_BPMNShape_StartEvent_2" bpmnElement="StartEvent_1">
            <dc:Bounds x="173" y="102" width="36" height="36" />
        </bpmndi:BPMNShape>
        </bpmndi:BPMNPlane>
    </bpmndi:BPMNDiagram>
    </bpmn:definitions>
    ''')
    return diagram

def modeler(request):

    bpmn_filename_url = 'https://raw.githubusercontent.com/bpmn-io/bpmn-js-examples/master/starter/diagram.bpmn'
    bpmn_filename_request = Request(bpmn_filename_url)
    bpmn_filename_handle = urlopen(bpmn_filename_request)
    bpmn_filename_content = bpmn_filename_handle.read()  

    data_dir = 'bpmndesigner_data'
    filename = 'diagram.bpmn'
    path = '{}/{}'.format(data_dir,filename)

    if default_storage.exists(path):
        storage_file = default_storage.open(path)
    else:
        content_file = ContentFile(bpmn_filename_content)    
        storage_file = default_storage.save(path, content_file)

    print(storage_file)

    context = {
        'bpmn_filename_url': bpmn_filename_url,
        'bpmn_filename_content':bpmn_filename_content,
        'storage_file':storage_file,
    }
    template = 'bpmndesigner/modeler.html'
    return render(request, template, context)    


def viewer(request, object_id):

    diagram = get_object_or_404(Diagram, pk=object_id)

    context = {
        'file_content': diagram.content,
    }
    template = 'bpmndesigner/viewer.html'
    return render(request, template, context) 

def index(request):
    diagrams = Diagram.objects.all()
    context = {
        'diagrams': diagrams,
    }
    template = 'bpmndesigner/index.html'
    return render(request, template, context) 

def edit(request, object_id):

    diagram = get_object_or_404(Diagram, pk=object_id)

    if request.method == 'POST':
        form = ModelerForm(request.POST)
        if form.is_valid():
            diagram.name = form.cleaned_data['name']
            diagram.content = form.cleaned_data['content']
            diagram.save()
            return redirect('bpmndesigner:edit', diagram.id)
    else:
        initial_data =  {
            'name': diagram, 
            'content':diagram.content
        }
        form = ModelerForm(initial_data)

    context = {
        'form': form,
        'diagram': diagram,
        'file_content': diagram.content,
    }
    template = 'bpmndesigner/edit.html'
    return render(request, template, context)
