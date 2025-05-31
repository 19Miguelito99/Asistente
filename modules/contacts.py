# Diccionario de contactos: nombre (en minúsculas) → correo electrónico
CONTACTOS = {
    "miguel": "juan.ejemplo@gmail.com",
    "": "",
    "ingeniero": "cmartinezb10@miumg.edu.gt",
    "": "",
    "juan": "juanprezmuralles@gmail.com",
}

def obtener_correo(nombre):
    """
    Retorna el correo asociado a un nombre si existe.
    """
    nombre = nombre.strip().lower()
    return CONTACTOS.get(nombre)
