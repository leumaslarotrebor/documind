from pypdf import PdfReader


def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    print(f"[INFO] Extracted text length: {len(text)}")
    return text
