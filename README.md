# Asistente de Auditoría de Sostenibilidad

Esta aplicación realiza auditorías de sostenibilidad usando Streamlit, LangChain, OpenAI Assistants, Firestore, Cloud Storage, y Neo4j AuraDB.

## 🚀 Despliegue en Google Cloud Run

### 1. Prepara tu entorno
- Crea un proyecto en GCP
- Habilita las APIs necesarias:
  - Firestore
  - Cloud Storage
  - Cloud Run
- Crea un bucket en Cloud Storage llamado `auditoria-informes`
- Configura Firestore en modo nativo

### 2. Autenticación
- Crea una cuenta de servicio con permisos para Firestore, Storage y Drive
- Descarga la clave JSON y llámala `credentials.json`

### 3. Despliegue con Docker

```bash
gcloud builds submit --tag gcr.io/<PROJECT-ID>/auditoria-app
gcloud run deploy auditoria-app   --image gcr.io/<PROJECT-ID>/auditoria-app   --platform managed   --region us-central1   --allow-unauthenticated
```

### 4. Variables de entorno

Configura en Cloud Run:

```
OPENAI_API_KEY=<tu-clave-OpenAI>
NEO4J_URI=neo4j+s://<tu-uri>.databases.neo4j.io
NEO4J_USER=neo4j
NEO4J_PASSWORD=<clave>
GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json
```

## 🧪 Estructura del proyecto

Ver `app.py`, `question_selector.py`, `firestore_client.py`, etc.

## 📝 Licencia

MIT
