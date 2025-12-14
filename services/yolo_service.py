from ultralytics import YOLO
from config import MODEL_PATH

VALID_YOLO_OBJECTS = {
    "person", "car", "bicycle", "motorcycle", "bus", "truck",
    "dog", "cat", "chair", "laptop", "book", "bottle", "cell phone",
    "backpack", "handbag", "cup", "tv", "keyboard"
}

yolo_model = YOLO(MODEL_PATH)


def analyze_image(filepath):
    try:
        results = yolo_model(filepath)

        detected = set()
        for box in results[0].boxes:
            cls_id = int(box.cls)
            label = results[0].names[cls_id].lower()

            if label in VALID_YOLO_OBJECTS:
                detected.add(label)

        return ", ".join(sorted(detected)) if detected else None

    except Exception as e:
        print("YOLO ERROR:", e)
        return None
