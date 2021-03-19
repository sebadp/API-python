from django.shortcuts import render
import requests
import json

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
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()
    s = requests.get(url.format(city))

    print(s.text)

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    print(city_weather)
    return render(request, 'api/index.html', {"city_weather": city_weather })