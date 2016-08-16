from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index),
    url(r'^result$', views.submit) ,
    url(r'^reset$', views.reset),
    url(r'^ninjas/(?P<id>\d+)$', views.show)  
]
