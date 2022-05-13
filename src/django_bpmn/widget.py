from django import forms


class BPMNWidget(forms.HiddenInput):
    template_name = 'django_bpmn/bpmn.html'
    input_type = 'hidden'

    class Media:
        css = {'all': ('https://unpkg.com/bpmn-js@9.0.3/dist/assets/diagram-js.css',
                       'https://unpkg.com/bpmn-js@9.0.3/dist/assets/bpmn-js.css',
                       'https://unpkg.com/bpmn-js@9.0.3/dist/assets/bpmn-font/css/bpmn.css',
                       '/static/django_bpmn/css/django_bpmn.css'),
               }
        js = ('https://unpkg.com/bpmn-js@9.0.3/dist/bpmn-modeler.development.js',)

        # css = {'all':('/static/django_bpmn/css/diagram-js.css',
        #               '/static/django_bpmn/css/bpmn-js.css',
        #               '/static/django_bpmn/css/bpmn.css',
        #               '/static/django_bpmn/css/django_bpmn'),}
        # js = ('/static/django_bpmn/js/bpmn-modeler.development.js',)
