import openai
import os
from firestore_client import get_progress

openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = "asst_informe"

def generate_audit_summary(session_id):
    progress = get_progress(session_id)
    questions = "\n".join([f"Q: {item['pregunta']}\nA: {item['respuesta']}" for item in progress])

    thread = openai.beta.threads.create()

    openai.beta.threads.messages.create(
        thread.id,
        role="user",
        content=f"Resume esta auditoría de sostenibilidad en un texto claro y profesional:\n\n{questions}"
    )

    run = openai.beta.threads.runs.create(thread.id, assistant_id=ASSISTANT_ID)

    import time
    while run.status != "completed":
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(thread.id, run.id)

    messages = openai.beta.threads.messages.list(thread.id)
    return messages.data[0].content[0].text.value
