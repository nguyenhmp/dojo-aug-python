from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    cities = models.Countries.objects.filter(languagetocountry__language='slovene')
    languages = models.Languages.objects.filter(language='slovene')
    mexico = models.Cities.objects.filter(country__name='Mexico').filter(population__gt=500000).order_by('-country__name')
    lang2 = models.Languages.objects.filter(percentage__gt=89).order_by('-country')
    test = models.Countries.objects.filter(surface_area__lt=501).filter(population__gt=100000)
    # prints the queries
    print (50*"*")
    print cities.query
    print (50*"*")
    print languages.query
    print (50*"*")
    print mexico.query
    print (50*"*")
    print lang2.query
    print (50*"*")
    print lang2.query
    print (50*"*")
    print test.query
    print (50*"*")
    return render(req, 'worldApp/index.html', context={'cities':cities, 'languages':languages, 'mexico':mexico, 'lang2':lang2, 'test':test})
