from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.modeler, name='modeler'),
    url(r'^modeler/$', views.modeler, name='modeler'),
    url(r'^viewer/$', views.viewer, name='viewer'),    
]