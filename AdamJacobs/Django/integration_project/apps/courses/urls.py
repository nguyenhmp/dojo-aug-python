from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='courses'),
    url(r'^process$', views.process, name='process'),
    url(r'^frankencourse$', views.frankencourse, name='frankencourse'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^user_courses$', views.user_courses, name='user_courses'),
]