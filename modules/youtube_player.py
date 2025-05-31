import pywhatkit

def reproducir_youtube(tema):
    try:
        pywhatkit.playonyt(tema)
        return f"Reproduciendo {tema} en YouTube."
    except Exception as e:
        return f"Error al reproducir: {e}"
