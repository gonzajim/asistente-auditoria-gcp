from google.cloud import storage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile

from firestore_client import get_progress

def generate_report(session_id):
    storage_client = storage.Client()
    bucket = storage_client.bucket("auditoria-informes")  # Asegúrate de que el bucket existe

    progress = get_progress(session_id)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        c = canvas.Canvas(tmp.name, pagesize=letter)
        c.drawString(100, 750, f"Informe de Auditoría - Sesión: {session_id}")
        y = 700
        for item in progress:
            c.drawString(100, y, f"Q: {item['pregunta']}")
            y -= 20
            c.drawString(120, y, f"A: {item['respuesta']}")
            y -= 40
        c.save()

        blob = bucket.blob(f"{session_id}/informe.pdf")
        blob.upload_from_filename(tmp.name)
        return blob.public_url
