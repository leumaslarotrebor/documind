from pypdf import PdfReader

def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    return text
