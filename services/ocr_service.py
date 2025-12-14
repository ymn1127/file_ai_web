import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_for_ocr(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(gray, -1, kernel)

    thresh = cv2.adaptiveThreshold(
        sharp, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )
    return thresh


def extract_text_from_image(path):
    try:
        img = preprocess_for_ocr(path)

        custom_config = r"--oem 1 --psm 6 -l kor+eng"

        data = pytesseract.image_to_data(img, config=custom_config, output_type=pytesseract.Output.DICT)

        valid_words = [
            data['text'][i]
            for i in range(len(data['text']))
            if int(data['conf'][i]) > 60 and len(data['text'][i].strip()) > 1
        ]

        if not valid_words:
            return "(이미지 내 텍스트 없음)"
        text = " ".join(valid_words)

        return text

    except Exception as e:
        print("OCR 실패:", e)
        return "(텍스트 없음 / OCR 실패)"
