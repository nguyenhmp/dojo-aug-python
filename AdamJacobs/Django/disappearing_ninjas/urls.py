from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tmnt$', views.index),
    url(r'^tmnt/ninjas/(?P<colors>\w*?)$', views.ninjas)
]