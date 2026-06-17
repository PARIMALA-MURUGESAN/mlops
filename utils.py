import pdfplumber
import docx

def extract_text(file):

    if file.name.endswith(".pdf"):
        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + " "

        return text.lower()

    elif file.name.endswith(".docx"):

        doc = docx.Document(file)

        text = ""

        for para in doc.paragraphs:
            text += para.text + " "

        return text.lower()

    else:
        return file.read().decode("utf-8").lower()
