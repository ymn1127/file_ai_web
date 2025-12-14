import fitz
import numpy as np
from PIL import Image
import easyocr
from config import OCR_LANGUAGES, OCR_USE_GPU

reader = easyocr.Reader(OCR_LANGUAGES, gpu=OCR_USE_GPU)


def extract_text_from_pdf(filepath):
    text = ""
    pdf = fitz.open(filepath)

    for page in pdf:
        raw = page.get_text()
        if raw.strip():
            text += raw + "\n"
            continue

        pix = page.get_pixmap(dpi=200)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        result = reader.readtext(np.array(img), detail=0)

        text += "\n".join(result) + "\n"

    pdf.close()
    return text.strip()
