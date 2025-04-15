from google.cloud import firestore

db = firestore.Client()

def save_response(session_id, question, answer):
    doc_ref = db.collection("auditorias").document(session_id)
    doc = doc_ref.get()
    data = doc.to_dict() if doc.exists else {"respuestas": []}
    data["respuestas"].append({"pregunta": question, "respuesta": answer})
    doc_ref.set(data)

def get_progress(session_id):
    doc = db.collection("auditorias").document(session_id).get()
    if doc.exists:
        return doc.to_dict().get("respuestas", [])
    return []
