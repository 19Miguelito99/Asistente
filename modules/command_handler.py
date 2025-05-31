from modules.weather import obtener_clima
from modules.file_search import buscar_archivos
from modules.email_sender import enviar_correo
from modules.app_launcher import abrir_aplicacion
from modules.youtube_player import reproducir_youtube
from modules.whatsapp_sender import enviar_whatsapp
from modules.gemini_connector import consultar_gemini

from modules.contacts import obtener_correo
from modules.voice_output import speak

from modules.voice_input import escuchar_comando

def procesar_comando(comando):
    comando = comando.lower()

    if "clima" in comando:
        speak("¿De qué ciudad deseas saber el clima?")
        ciudad = escuchar_comando()
        return obtener_clima(ciudad)

    elif "buscar archivo" in comando:
        speak("¿Qué tipo de archivo deseas buscar? Por ejemplo, PDF o TXT.")
        extension = escuchar_comando()
        return buscar_archivos(extension)

    elif "correo" in comando:
        speak("¿A quién deseas enviar el correo?")
        nombre = escuchar_comando()
        destinatario = obtener_correo(nombre)

        speak("¿Cuál es el asunto del correo?")
        asunto = escuchar_comando()

        speak("¿Qué deseas escribir en el cuerpo del correo?")
        mensaje = escuchar_comando()

        return enviar_correo(destinatario, asunto, mensaje)

    elif "abrir" in comando:
        speak("¿Qué aplicación deseas abrir?")
        app = escuchar_comando()
        return abrir_aplicacion(app)

    elif "youtube" in comando:
        speak("¿Qué canción o video deseas reproducir?")
        video = escuchar_comando()
        return reproducir_youtube(video)

    elif "whatsapp" in comando:
        speak("¿A qué número deseas enviar el mensaje? Incluye el código del país.")
        numero = escuchar_comando()

        speak("¿Qué mensaje deseas enviar?")
        mensaje = escuchar_comando()

        return enviar_whatsapp(numero, mensaje)

    elif "gemini" in comando or "gemini" in comando:
        if any(palabra in comando for palabra in ["entrar", "activar", "usar", "consultar"]):
            return consultar_gemini("consultar Gemini")
        else:
            return "Hola, soy Gemini. ¿En qué puedo ayudarte?"

    else:
        return consultar_gemini(comando)