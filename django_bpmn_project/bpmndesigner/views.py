# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import BPMN
from os import defpath
import os

# Create your views here.

def modeler(request):

    bpmn_filename = 'https://cdn.rawgit.com/bpmn-io/bpmn-js-examples/dfceecba/starter/diagram.bpmn'
    context = {'bpmn_filename': bpmn_filename}
    template = 'bpmndesigner/modeler.html'
    return render(request, template, context)    

def list_bpmn(request):
    bpmn_list = BPMN.objects.all()
    context = {"bpmn_list":bpmn_list}
    template = 'bpmndesigner/list.html'
    return render(request, template, context)

def create_bpmn(request):
    bpmn_filename =  os.path.join(settings.BASE_DIR, 'bpmndesigner', 'static', 'diagrams', 'default.bpmn')
    with open(bpmn_filename, 'r') as f:
        bpmn_file_content = f.read()
    context = {'bpmn_filename': bpmn_filename, 'bpmn_file_content': bpmn_file_content, 'id_bpmn': -1}
    template = 'bpmndesigner/modeler.html'
    return render(request, template, context)

def save_bpmn(request):
    try:
        # here comes validations, permissions check, ...
        id = request.POST.get("id")
        name = request.POST.get("name")
        xml_content = request.POST.get("xml_content")
        if id and id != '-1': # if id was given, then update the diagram and don't create a new one
            qs = BPMN.objects.filter(id=id)
            if qs.exists():
                bpmn = qs[0]
                bpmn.xml_content = xml_content
                bpmn.save()
                result_msg = "BPMN updated sucessfully!"
                result_status = 2  # TODO: create an enum or choices to hold this status values
        else: # create a new diagram
            bpmn = BPMN.objects.create(name=name, xml_content=xml_content)
            bpmn.save()
            result_msg = "BPMN saved sucessfully!"
            result_status = 1  # TODO: create an enum or choices to hold this status values

    except Exception as err: # TODO: create many specific validations to every possible scenario
        print(err)
        result_msg = err.message
        result_status = 0

    return HttpResponse(content_type="application/json", content='{"status":"%d", "msg":"%s"}' % (result_status, result_msg))

def open_bpmn(request, id):
    try:
        qs = BPMN.objects.filter(id=id)
        if qs.exists():
            bpmn = qs[0]
            bpmn_file_content = bpmn.xml_content
            context = {'bpmn_file_content':bpmn_file_content, 'id_bpmn':bpmn.id}
            template = 'bpmndesigner/modeler.html'
            return render(request, template, context)

    except Exception as err: #TODO: implement specific exception for each error situation with specific error handling
        print(err)

def delete_bpmn(request, id):
    try:
        qs = BPMN.objects.filter(id=id)
        if qs.exists():
            name = qs[0].name
            msg = u"Diagram '%s' deleted successfully!" % name
            qs.delete()
        else:
            msg = None
            tag_msg = None
        tag_msg = 'success'
    except Exception as err:
        msg = err.message
        tag_msg = 'error'
    bpmn_list = BPMN.objects.all()
    context = {'bpmn_list':bpmn_list, 'msg': msg, 'tag_msg': tag_msg}
    template = 'bpmndesigner/list.html'
    return render(request, template, context)
