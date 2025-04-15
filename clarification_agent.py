import openai
import os
import time

openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = "asst_2"  # Reemplaza por el ID real del Assistant de aclaraciones

def get_clarification(question):
    thread = openai.beta.threads.create()

    openai.beta.threads.messages.create(
        thread.id,
        role="user",
        content=f"Por favor, aclara el siguiente concepto de sostenibilidad: {question}"
    )

    run = openai.beta.threads.runs.create(thread.id, assistant_id=ASSISTANT_ID)

    while run.status != "completed":
        time.sleep(1)
        run = openai.beta.threads.runs.retrieve(thread.id, run.id)

    response = openai.beta.threads.messages.list(thread.id)
    answer = response.data[0].content[0].text.value
    return answer
