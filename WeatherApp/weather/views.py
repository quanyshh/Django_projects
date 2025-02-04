from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    appid = '0524b363da8977c2d2594bb6fdae7c9b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []
    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info':all_cities, 'form':form}
    print(context)

    return render(request, 'weather/index.html', context)
