import modules.voice_input as vi
import modules.voice_output as vo
from modules.command_handler import procesar_comando

PALABRA_CLAVE = "wanda"  # o "hey asistente"

def main():
    vo.speak("Asistente activado. Di 'wanda' para comenzar.")
    while True:
        print("Escuchando palabra clave...")
        activacion = vi.escuchar_comando()
        if activacion and PALABRA_CLAVE in activacion.lower():
            vo.speak("Te escucho.")
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

