from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

import database  # ← 안전 import 방식

from config import UPLOAD_FOLDER
from services.ocr_service import extract_text_from_image
from services.pdf_service import extract_text_from_pdf
from services.txt_service import extract_text_from_txt
from services.yolo_service import analyze_image
from services.tag_service import generate_text_tags, merge_tags

database.init_db()

app = Flask(__name__)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    msg = request.args.get("msg", "")
    ocr = request.args.get("ocr", "")
    file_count = database.get_file_count()

    return render_template("index.html",
                           msg=msg,
                           ocr=ocr,
                           file_count=file_count)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if not file or file.filename.strip() == "":
        return redirect(url_for("index", msg="⚠ 파일이 선택되지 않았습니다"))

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    ext = filename.lower()
    text = ""
    filetype = "unknown"

    if ext.endswith(".pdf"):
        text = extract_text_from_pdf(filepath)
        filetype = "pdf"

    elif ext.endswith(".txt"):
        text = extract_text_from_txt(filepath)
        filetype = "text"

    elif ext.endswith((".jpg", ".jpeg", ".png")):
        text = extract_text_from_image(filepath)
        filetype = "image"

    text_tags = generate_text_tags(text)
    ai_tags = analyze_image(filepath)
    tags = merge_tags(text_tags, ai_tags)

    summary = text.strip()[:200] if text.strip() else "(텍스트 인식 실패)"

    database.insert_file(filename, filetype, tags, summary, filepath)

    return redirect(url_for("index", msg="📌 업로드 완료!", ocr=summary))


@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword", "").strip()
    results = database.search_files(keyword)
    file_count = database.get_file_count()

    return render_template("results.html",
                           keyword=keyword,
                           results=results,
                           file_count=file_count)


@app.route("/detail/<filename>")
def detail(filename):
    file = database.get_file_detail(filename)
    return render_template("detail.html", file=file)


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
