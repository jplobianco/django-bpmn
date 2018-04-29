# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import requests 

from urllib2 import Request, urlopen

from xml.dom import minidom

from .models import Diagram

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


def viewer(request):

    data_dir = 'bpmndesigner_data'
    filename = 'diagram.bpmn'
    path = '{}{}/{}'.format(settings.MEDIA_ROOT, data_dir, filename)

    f = open(path)
    file_content = f.read()
    print(file_content)

    diagram = Diagram.objects.create(name='Teste1',content=file_content)

    context = {
        'bpmn_filename_url':  path,
        'file_content': diagram.content,
    }
    template = 'bpmndesigner/viewer.html'
    return render(request, template, context) 


