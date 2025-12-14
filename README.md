## AI 기반 파일 분석 시스템


# Python 버전
- Python **3.10.x**

# 사용 라이브러리 및 버전

| 라이브러리 | 버전 |
| Flask | 3.1.2 |
| SQLite | 내장 |
| pytesseract | 0.3.13 |
| Tesseract OCR | 5.5.0 |
| EasyOCR | 1.7.2 |
| OpenCV | 4.12.0 |
| PyMuPDF | 1.26.6 |
| Ultralytics YOLO | 8.3 |
| Pillow | 12.0 |
| NumPy | 2.2.6 |

# Tesseract OCR 설치 (Windows)
- https://github.com/tesseract-ocr/tesseract
- 설치 후 `tesseract.exe` 경로를 `ocr_service.py`에 설정

# 실행 방법
1. 가상환경 생성
python -m venv .venv

2. 가상환경 활성화
.venv\Scripts\activate

3. 라이브러리 설치
pip install -r requirements.txt

4. 서버 실행 후 브라우저 접속
python app.py
http://127.0.0.1:5000
