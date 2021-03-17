"""
Consumir html's con la librería requests
"""
# import requests

# if __name__ == '__main__':
#     url = 'https://www.google.com/'
#     response = requests.get(url)
#     """
#     Si imprimimos esto nos respondería con un response
#     print(response)
#     >>josela@josela-Satellite-L655:~/API-python$ python3 main.py
#     >><Response [200]>
#     """

#     if response.status_code == 200:
#         """
#         El argumento .content nos devuelve en este caso todo el contenido HTML
#         Si queremos guardarlo en un archivo aparte tendíamos que hacer:
#         """
#         content = response.content
#         file = open('google.html', 'wb')
#         file.write(content)
#         file.close()
#         print(response.content)

"""
Vamos a obtener JSON e imprimir sus atributos
"""

# import requests

# if __name__ == '__main__':
#     url = 'https://httpbin.org/get'
#     args = {'nombre':'seba', 'curso': 'python'}
#     """
#     Le mandamos parametros con el diccionario args, y los vemos pasandole el argumento params=''
#     """
#     response = requests.get(url, params=args)


#     if response.status_code == 200:
#         """
#         El argumento .content nos devuelve en este caso todo el contenido JSON
#         """
#         content = response.content
        
#         print(content)
#         # si quiero imprimir el atributo url de response:
#         print(response.url)

#         # para trabajarlo como JSON:
#         response_json=response.json()
#         print(response_json)
#         # para imprimir los artibutos puedo usar la sintaxis nombreVar['']
#         print(response_json['args'])        
#         print(response_json['origin'])
#         print(response_json['headers'])

"""
Vamos a imprimir JSON y sus atributos pero además usando la librería de python: JSON
"""

# import requests
# import json

# if __name__ == '__main__':
#     url = 'https://httpbin.org/get'
#     response = requests.get(url)


#     if response.status_code == 200:
#         response_json = json.loads(response.text)
#         print(response_json['origin'])

"""
El método POST
"""
"""
Vamos a imprimir JSON y sus atributos pero además usando la librería de python: JSON
"""

# import requests
# import json

# if __name__ == '__main__':
#     url = 'https://httpbin.org/post'
#     payload = {'nombre':'seba', 'curso': 'python'}
#     """
#     Le mandamos parametros con el diccionario payload, y los pasamos con el argumento json=''
#     """
#     headers= {'sarasa': 'sarasa'}
#     """
#     SI queremos agregar algún elemento a headers, lo hacemos con post, 
#     agregandole datos al diccionario, hay que hacerlo antes de hacer el post.
    
#     """
#     response = requests.post(url, json=payload, headers=headers)
#     print(response.url)

#     if response.status_code == 200:
#         response_json = json.loads(response.text)
#         print(response_json)
#         print(response_json['headers'])
#         # headers_response = response_json.headers
#         response_headers = response.headers
#         print(response_headers)
"""
CONSUMIR API POKEMON
Vamos a listar una serie de pokemons
"""

# import requests
# import json

# if __name__ == '__main__':
#     url = 'https://pokeapi.co/api/v2/pokemon'
#     args={'offset': '80'}
#     response = requests.get(url, params=args)
#     # print(response.content)

#     if response.status_code == 200:
#         payload = response.json()
#         # vamos a hacer una lista vacía si no encuentra resultados, eso lo indicamos con una lista vacía como 
#         # opción si no encuentra "results"
#         # por defecto esta API te devuelve una lista de 20 resultados y las pagina
#         # para modificar esto hay que pasarle el parametro offset
#         result = payload.get('results', [])
#         # print(result)
#         if result:
#             for pokemon in result:
#                 name = pokemon['name']
#                 print(name)

"""
CONSUMIR API POKEMON
Vamos a listar una serie de pokemons
de una forma más compleja, creando una funcion para no repetirnos y tener un buscador de pokemons.
"""

import requests
import json


def get_pokemons(url='https://pokeapi.co/api/v2/pokemon', offset=0):
    args = {'offset': offset} if offset else {}

    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        result = payload.get('results', [])
        # print(result)
        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)

        next = input("continuamos listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon'
    # args={'offset': '80'}
    # response = requests.get(url, params=args)
    # print(response.content)
    get_pokemons()