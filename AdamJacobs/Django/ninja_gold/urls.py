from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninjagold$', views.index),
    url(r'^ninjagold/process_money/(?P<building>\w*?)$', views.process_money),
]