import modules.voice_input as vi
import modules.voice_output as vo
from modules.command_handler import procesar_comando

def main():
    vo.speak("Asistente activado. ¿En qué puedo ayudarte?")
    while True:
        comando = vi.escuchar_comando()
        if comando:
            if "salir" in comando.lower():
                vo.speak("Hasta luego.")
                break
            respuesta = procesar_comando(comando)
            if respuesta:
                vo.speak(respuesta)

if __name__ == "__main__":
    main()
