from django.conf.urls import url, include
from . import views    

urlpatterns = [             
    url(r'^$', views.index), #route to your homepage always. views. "index" -> refers to your function in views.py in your app. 
    # url(r'^users$', views.show) 
]
