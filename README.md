# django-bpmn

Encapsulates the [bpmn-js](https://github.com/bpmn-io/bpmn-js.git) modeler into a Django widget. 
This is not part of the oficial [bpmn-io](https://github.com/bpmn-io/) initiative. 
Take a look at their [license](https://raw.githubusercontent.com/bpmn-io/bpmn-js/develop/LICENSE), specially the explicit forbidden to hide their watermark.


## Usage

Install the dependency ```pip install django-bpmn```

Add 'django_bpmn' to _INSTALLED_APPS_

In a text field in your form add the _widget=BPMNWidget_

 ```python
from django import forms
from django_bpmn.widget import BPMNWidget

from sample.models import BPMN


class BPMNForm(forms.Form):
    diagram = forms.CharField(widget=BPMNWidget)


class BPMNModelForm(forms.ModelForm):
    diagram = forms.CharField(widget=BPMNWidget)

    class Meta:
        model = BPMN
        exclude = ()

 ```

The model attibute that store the attribute should be a blob type like TextField.

```python
from django.db import models


class BPMN(models.Model):
    diagram = models.TextField('Diagram')

```


## Sample

```
docker run -p 8000:8000 jplobianco/django-bpmn-sample
```

Access your browser at _localhost:8000_.