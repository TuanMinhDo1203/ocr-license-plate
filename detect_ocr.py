import cv2
import pytesseract
import re
from ultralytics import YOLO

# Cấu hình đường dẫn Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load YOLOv8 model
model = YOLO("runs/detect/train/weights/best.pt")

# Hậu xử lý văn bản biển số
def smart_correction(text):
    text = text.upper().strip()
    text = text.replace("!", "1").replace("I", "1").replace("L", "1")
    text = text.replace("O", "0").replace("S", "5")
    text = text.replace("6", "G").replace("G", "6") if "G" not in text[:3] else text
    text = re.sub(r"[^A-Z0-9\-]", "", text)

    if "-" not in text and len(text) >= 6:
        text = text[:3] + "-" + text[3:]
    return text

# Pipeline chính
def detect_and_ocr(image_bgr):
    img_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    results = model(img_rgb)[0]
    boxes = results.boxes.xyxy.cpu().numpy().astype(int)

    outputs = []
    for (x1, y1, x2, y2) in boxes:
        plate_crop = img_rgb[y1:y2, x1:x2]

        # Resize và chuyển grayscale
        plate_crop = cv2.resize(plate_crop, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(plate_crop, cv2.COLOR_RGB2GRAY)

        # OCR
        text_raw = pytesseract.image_to_string(gray, config="--psm 7")
        text_cleaned = smart_correction(text_raw)

        outputs.append({
            "crop": plate_crop,
            "text_raw": text_raw.strip(),
            "text_cleaned": text_cleaned
        })
    return outputs
