import subprocess

def abrir_aplicacion(nombre):
    nombre = nombre.lower().strip()

    # Diccionario de aplicaciones comunes
    rutas_comunes = {
        "bloc de notas": "notepad",
        "calculadora": "calc",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
        "excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
        "cmd": "cmd",
        "powershell": "powershell",
        "spotify": "spotify",
        "disney plus": "start shell:AppsFolder\\Disney.37853FC22B2CE_6rarf9sa4v8jt!App",
        "netflix": "start shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!App"
    }

    # Obtener el comando/ruta
    ruta = rutas_comunes.get(nombre)

    if ruta:
        try:
            subprocess.Popen(ruta, shell=True)
            return f"Abriendo {nombre}..."
        except Exception as e:
            return f"No se pudo abrir '{nombre}': {str(e)}"
    else:
        return f"No se encontró la aplicación '{nombre}'. Verifica el nombre o agrega su ruta al diccionario."
