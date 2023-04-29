from fastapi import FastAPI
from fastapi.responses import StreamingResponse 

import requests

app = FastAPI()

# Define los detalles de la API
# url = "https://api.openai.com/v1/chat/completions"
# model_engine = "text-davinci-003"

# Get models 
    # url2 = "https://api.openai.com/v1/engines"
    # res  = requests.get(f"{url2}", headers=headers)

    
url = "https://api.openai.com/v1/engines/code-davinci-edit-001/completions"
model_engine = "code-davinci-edit-001"

api_key = ""

# Función que envía la pregunta a la API y recibe la respuesta
@app.get("/generar_respuesta")
def generar_respuesta(pregunta):
    # Define los parámetros de la solicitud
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "prompt": pregunta,
        "temperature": 0.7,
        "max_tokens": 100,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    # Envía la solicitud a la API
    response = requests.post(f"{url}/{model_engine}", headers=headers, json=payload)
    # Procesa la respuesta de la API y devuelve la respuesta generada
    respuesta_generada = response.json()["choices"][0]["text"]
    return respuesta_generada

# # Ejecuta el script para responder preguntas
# while True:
#     # Pide una pregunta al usuario
#     pregunta = input("Haz una pregunta: ")
#     # Genera una respuesta a la pregunta utilizando la función definida anteriormente
#     respuesta_generada = generar_respuesta(pregunta)
#     # Muestra la respuesta generada al usuario
#     print(respuesta_generada)
