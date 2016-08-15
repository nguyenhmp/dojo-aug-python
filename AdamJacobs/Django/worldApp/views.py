from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    cities = models.Countries.objects.filter(languagetocountry__language='slovene')
    languages = models.Languages.objects.filter(language='slovene')
    # countcities = models.Cities.objects.count()
    mexico = models.Cities.objects.filter(country__name='Mexico').filter(population__gt=500000).order_by('-country__name')
    lang2 = models.Languages.objects.filter(percentage__gt=89).order_by('-country')
    popsurf = models.Countries.objects.filter(surface_area__lt=501).filter(population__gt=100000)
    constmarch = models.Countries.objects.filter(government_form='Constitutional Monarchy').filter(capital__gt=200).filter(life_expectancy__gt=75)
    argentina = models.Cities.objects.filter(country__name='Argentina').filter(district='Buenos Aires').filter(population__gt=500000)
    countcities = models.Countries.objects.raw('SELECT countries.name, countries.id, COUNT(cities.name) AS count FROM countries LEFT JOIN cities ON countries.code=cities.country_code GROUP BY countries.id')
    countregion = models.Countries.objects.raw('SELECT id, region, COUNT(id) AS count FROM countries GROUP BY region ORDER BY count DESC')
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
    print popsurf.query
    print (50*"*")
    print countcities
    print (50*"*")
    print countregion
    print (50*"*")
    return render(req, 'worldApp/index.html', context={'cities':cities, 'languages':languages, 'mexico':mexico, 'lang2':lang2, 'popsurf':popsurf, 'constmarch':constmarch, 'argentina':argentina, 'countcities':countcities, 'countregion':countregion})
