import subprocess

def abrir_aplicacion(nombre):
    try:
        subprocess.Popen(nombre)
        return f"Abriendo {nombre}"
    except Exception as e:
        return f"No se pudo abrir {nombre}: {e}"
