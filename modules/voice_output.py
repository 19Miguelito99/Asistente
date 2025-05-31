import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(texto):
    print("Asistente:", texto)
    engine.say(texto)
    engine.runAndWait()

