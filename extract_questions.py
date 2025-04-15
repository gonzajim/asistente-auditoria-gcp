from docx import Document

def extract_questions_from_docx(file_path):
    doc = Document(file_path)
    questions = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text.endswith('?'):
            questions.append(text)
    return questions
