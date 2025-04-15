import streamlit as st
from firestore_client import save_response, get_progress
from question_selector import get_next_question
from clarification_agent import get_clarification
from report_generator import generate_report
from openai import OpenAI
import os

st.set_page_config(page_title="Auditoría Sostenible", layout="wide")

st.title("Auditor de Sostenibilidad Recava")

session_id = st.text_input("Introduce tu identificador de sesión:")

if session_id:
    progress = get_progress(session_id)
    current_question = get_next_question(session_id, progress)

    # Mostrar progreso
    st.markdown(f"**Progreso: {len(progress)} preguntas respondidas**")
    st.progress(len(progress) / 20)  # Asume 20 preguntas como base

    st.markdown("### Pregunta actual:")
    st.info(current_question)

    answer = st.text_area("Tu respuesta:")

    if st.button("Enviar respuesta"):
        save_response(session_id, current_question, answer)
        st.experimental_rerun()

    if st.button("¿Necesitas aclaración?"):
        clarification = get_clarification(current_question)
        st.success(clarification)

    if st.button("Finalizar auditoría y generar informe"):
        file_url = generate_report(session_id)
        st.success(f"Informe generado: [Descargar informe]({file_url})")
        st.markdown(f"[Descargar informe de auditoría]({file_url})")
