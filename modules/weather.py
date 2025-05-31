import requests
from config import WEATHER_API_KEY

def obtener_clima(ciudad="Guatemala"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={WEATHER_API_KEY}&lang=es&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        descripcion = data["weather"][0]["description"]
        temperatura = data["main"]["temp"]
        return f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C"
    else:
        return "No se pudo obtener el clima en este momento."
