# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BPMN(models.Model):
    xml_content = models.TextField(max_length=0)
    name = models.CharField(max_length=255)
    # TODO: add create_time, owner, ...