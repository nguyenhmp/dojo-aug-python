from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='random'),
    url(r'^create$', views.create, name='new_word')
]