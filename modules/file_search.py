import os

def buscar_archivos(extension, ruta="C:\\"):
    encontrados = []
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(f".{extension}"):
                encontrados.append(os.path.join(carpeta, archivo))
        if len(encontrados) >= 3:
            break
    if encontrados:
        return f"Se encontraron archivos como: {', '.join(encontrados[:3])}"
    else:
        return "No se encontraron archivos."
