# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Diagram

# Register your models here.


class DiagramAdmin(admin.ModelAdmin):

    list_display = ('name','view_diagram',)

    def view_diagram(self, obj):
        # return ("%s %s" % (obj.name, obj.name)).upper()
        # return '<a href="{% url \'bpmndesigner:viewer\' %}">OPEN VIEWER</a>'
        return '<a href="www.uol.com.br"\a>'
    view_diagram.short_description = 'View diagram'    

    # list_display = ('name', 'view_diagram')

    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'view_diagram')
    #     }),
        
    # )

    

    # def view_diagram(self, obj):
    #     return '<a href="%s">%s</a>' % (obj.view_diagram, obj.view_diagram)
    # view_diagram.allow_tags = True


admin.site.register(Diagram,DiagramAdmin)

