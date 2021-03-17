import requests

if __name__ == '__main__':
    url = 'https://www.google.com/'
    response = requests.get(url)
    """
    Si imprimimos esto nos respondería con un response
    print(response)
    >>josela@josela-Satellite-L655:~/API-python$ python3 main.py
    >><Response [200]>
    """

    if response.status_code == 200:
        """
        El argumento .content nos devuelve en este caso todo el contenido HTML
        Si queremos guardarlo tendíamos que hacer:
        """
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()
        print(response.content)