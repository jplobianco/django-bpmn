from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^modeler/$', views.modeler, name='modeler'),
    url(r'^view/(?P<object_id>[0-9]+)/$', views.viewer, name='viewer'),
    url(r'^edit/(?P<object_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^svg/(?P<object_id>[0-9]+)/$', views.view_svg, name='view_svg'),
]