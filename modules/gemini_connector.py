import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(model_name='gemini-pro')

def consultar_gemini(pregunta):
    respuesta = model.generate_content(pregunta)
    return respuesta.text
