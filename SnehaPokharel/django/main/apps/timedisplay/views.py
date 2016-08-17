from django.shortcuts import render, HttpResponse

from datetime import datetime
TIME_ZONE = 'America/New_York'

print "*"*12
print "*"*12

def index(request): #this is where your methods and functions will go. just like in flask, you can return multiple parameters including dictionary which allows you to use django rendering templates to pass vairables. 
    context = {"time" : datetime.now().strftime('%m/%d/%Y   %I:%M:%S %p')}
    return render(request, "randomword/index.html", context)
