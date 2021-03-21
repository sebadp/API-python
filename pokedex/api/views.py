from django.shortcuts import render, redirect
import requests
import json
from .models import City
from .forms import CityForm
# Create your views here.

def home(request):
    # response = requests.get('https://pokeapi.co/api/v2/pokemon/')
    # print(response)
    # responsea = requests.get('api.openweathermap.org/data/2.5/weather?q={}&APPID=f90ad0886c327876a42b2994b9e62f46')
    # response2= responsea.json()
    # print(response2)
    # if response.status_code == 200:
    #     payload = response.json()
    #     result = payload.get('results', [])
    # # print(result)
    #     if result:
    #         for pokemon in result:
    #             name = pokemon['name']
    #             print(name)
    url= 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=f90ad0886c327876a42b2994b9e62f46'

    err_msg = ''

    message = ''

    msg_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)
        
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name='new_city').count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'Ingrese un nombre de Ciudad Válido.'
            else:
                err_msg = 'Esta Ciudad ya está en la Base de Datos!'

        if err_msg:
            message = err_msg
            msg_class = 'is-danger'
        else:
            message = 'La Ciudad se agregó con éxito!'
            msg_class = 'is-success'
    form = CityForm()

    cities= City.objects.all()

    weather_data = []
    context = {
        'form': form,
        'weather_data': weather_data,
        'message': message,
        'msg_class': msg_class,
    }
    # r = requests.get(url.format(city)).json()
    # s = requests.get(url.format(city))

    # print(s.text)

    for city in cities: 

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    print(weather_data)
    return render(request, 'api/index.html', context)

def removeCity(request, city):
    City.objects.get(name=city).delete()
    return redirect('home')