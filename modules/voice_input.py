import speech_recognition as sr

def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES")
        print(f"Tú dijiste: {comando}")
        return comando
    except sr.UnknownValueError:
        print("No entendí.")
        return ""
    except sr.RequestError:
        print("Error de conexión con el servicio de reconocimiento.")
        return ""
