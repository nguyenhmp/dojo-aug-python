from django.conf.urls import url, include
#you only change this to include routes to specific apps that you created. This is the main urls!

urlpatterns = [
    url(r'^', include('apps.wallERD.urls'))
]
