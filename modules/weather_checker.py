import requests
from config import WEATHER_API_KEY

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={WEATHER_API_KEY}&units=metric&lang=es"
    r = requests.get(url)
    data = r.json()
    if r.status_code == 200:
        temp = data['main']['temp']
        descripcion = data['weather'][0]['description']
        return f"El clima en {ciudad} es {descripcion} con {temp} grados Celsius."
    else:
        return "No pude obtener el clima."
