from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^loginandreg$', views.index),
    url(r'^registration$', views.register),
    url(r'^login$', views.login),
    url(r'^loginandreg/success$', views.success),
]