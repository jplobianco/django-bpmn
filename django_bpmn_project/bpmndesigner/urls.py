from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.modeler, name='modeler'),
    url(r'^modeler/$', views.modeler, name='modeler'),
    url(r'^viewer/(?P<object_id>[0-9]+)/$', views.viewer, name='viewer'),        
]