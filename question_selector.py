import openai
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = "asst_1"  # Reemplaza por el ID real del Assistant de selección de preguntas

def get_next_question(session_id, history):
    thread = openai.beta.threads.create()

    messages = [
        {"role": "system", "content": "Eres un sistema que guía una auditoría de sostenibilidad."},
        {"role": "user", "content": f"Historial: {history}. ¿Cuál es la siguiente pregunta lógica?"}
    ]

    for msg in messages:
        openai.beta.threads.messages.create(thread.id, role=msg["role"], content=msg["content"])

    run = openai.beta.threads.runs.create(thread.id, assistant_id=ASSISTANT_ID)

    while run.status != "completed":
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(thread.id, run.id)

    response = openai.beta.threads.messages.list(thread.id)
    answer = response.data[0].content[0].text.value
    return answer
