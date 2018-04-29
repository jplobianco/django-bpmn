# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Diagram(models.Model):
    name = models.CharField("Name", max_length=255, null=False, blank=False)
    content = models.TextField("Content", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Diagram'
        verbose_name_plural = 'Diagrams'    