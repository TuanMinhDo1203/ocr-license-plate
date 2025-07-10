
# 🚗 Vietnamese License Plate OCR with YOLOv8 + Tesseract

This project detects and extracts **vehicle license plate numbers** from images using a two-stage pipeline:  
🔹 **YOLOv8** for license plate detection  
🔹 **Tesseract OCR** for text recognition

<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/plate-demo.gif" width="600">
</p>

---

## 📌 Project Goals

- Detect vehicle license plates from input images.
- Apply OCR to extract the text from detected regions.
- Improve OCR accuracy with preprocessing and post-processing.
- Build a simple web interface for demonstration (using Streamlit).

---

## 🔍 System Architecture

```mermaid
flowchart LR
    A[Input Image] --> B[YOLOv8 Detection]
    B --> C[Crop License Plate]
    C --> D[Tesseract OCR]
    D --> E[Post-processing - Error Correction]
    E --> F[Display Final Text]
```
---

## 📁 Project Structure

```
license-plate-ocr/
├── app.py                  # Streamlit web interface
├── detect_ocr.py           # Main OCR pipeline
├── requirements.txt        # Python dependencies
├── test_images/            # Sample images for testing
├── runs/                   # Trained YOLOv8 model (best.pt)
└── README.md               # This file
```

---

## 🚀 Getting Started

### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Launch Streamlit app

```bash
streamlit run app.py
```

---

## 🖼️ Example Results

![App Screenshot](screenshot/Capture.JPG)

---

## 🛠️ Tech Stack

| Component       | Tool/Library         |
| --------------- | -------------------- |
| Detection       | YOLOv8 (Ultralytics) |
| OCR             | Tesseract            |
| Post-processing | Python + Regex       |
| Web Interface   | Streamlit            |

---

## 📊 Performance

* The pipeline gives good OCR results on images similar to the training conditions.
* YOLOv8 was trained on a custom dataset captured in parking exit scenarios:
  - Top-down or slightly angled views from surveillance cameras
  - Vehicles exiting parking lots
  - Daylight conditions, moderate image resolution
  - Vietnamese-style license plates



<p align="center">
  <img src="screenshot/data2.JPG" width="800">
</p>

* For best results, input images should be similar in angle and clarity to the training data.
* Common OCR mistakes (e.g., `0 ↔ O`, `5 ↔ S`) are handled by post-processing rules.


---

## 💼 Real-world Applications

* Automated entry/exit systems in parking lots.
* Traffic camera plate reading.
* Vehicle tracking in smart cities.

---

## 👤 Author

* **Name**: Do Tuan Minh
* **Role**: AI student & developer of this pipeline and interface

---

## ⭐ Like this project?

If you find this helpful, consider giving it a **⭐ Star** to support the work!

.

