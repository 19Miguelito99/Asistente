import google.generativeai as genai
from config import GEMINI_API_KEY

# Configura tu clave de API desde config.py
genai.configure(api_key=GEMINI_API_KEY)

# Usa el modelo "gemini-2.0-flash", más rápido y económico
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def consultar_gemini(pregunta):
    try:
        response = model.generate_content(pregunta)
        return response.text  # Puede lanzar error si el resultado está vacío
    except Exception as e:
        return f"Ocurrió un error al consultar Gemini: {str(e)}"
