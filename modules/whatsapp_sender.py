import pywhatkit
import datetime

def enviar_whatsapp(numero, mensaje):
    try:
        hora = datetime.datetime.now()
        pywhatkit.sendwhatmsg(numero, mensaje, hora.hour, hora.minute + 2)
        return f"Mensaje programado a {numero}."
    except Exception as e:
        return f"No se pudo enviar el mensaje: {e}"
