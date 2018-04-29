from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_bpmn, name='list_bpmn'),
    url(r'^save_bpmn/', views.save_bpmn, name='save_bpmn'),
    url(r'^create_bpmn/', views.create_bpmn, name="create_bpmn"),
    url(r'^open_bpmn/(\d+)/$', views.open_bpmn, name="open_bpmn"),
    url(r'^delete_bpmn/(\d+)/$', views.delete_bpmn, name="delete_bpmn"),
    url(r'^modeler/', views.modeler, name='modeler'),
]