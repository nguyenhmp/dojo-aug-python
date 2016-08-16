from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index),
    url(r'^process/(?P<button>[a-zA-Z]+)$', views.show),
    url(r'^reset$', views.reset) 
]
