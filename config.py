import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DB_NAME = os.path.join(BASE_DIR, "filedata.db")
MODEL_PATH = os.path.join(BASE_DIR, "models", "yolov8n.pt")

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
OCR_LANGUAGES = ["ko", "en"]
OCR_USE_GPU = False
