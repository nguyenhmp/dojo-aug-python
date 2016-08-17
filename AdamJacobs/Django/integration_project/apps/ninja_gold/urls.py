from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='ninjagold'),
    url(r'^process_money/(?P<building>\w*?)$', views.process_money, name='process_money'),
]