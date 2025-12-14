def extract_text_from_txt(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except:
        try:
            with open(filename, "r", encoding="cp949") as f:
                text = f.read()
        except:
            return ""
    return text.strip()
