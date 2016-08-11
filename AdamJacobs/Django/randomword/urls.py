from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random$', views.index),
    url(r'^create$', views.create)
]