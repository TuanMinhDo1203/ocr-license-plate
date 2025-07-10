Dưới đây là toàn bộ nội dung `README.md` ở dạng **Markdown đầy đủ** bạn có thể copy dán vào file `README.md` trong repo GitHub:

---

````markdown
# 🚗 License Plate OCR with YOLOv8 + Tesseract

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
    D --> E[Post-processing (Error Correction)]
    E --> F[Display Final Text]
````

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

| Original Image               | OCR Result  |
| ---------------------------- | ----------- |
| ![](test_images/sample1.jpg) | `51G-47281` |
| ![](test_images/sample2.jpg) | `29A-12345` |

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

* OCR accuracy after post-processing: **\~90%+** on clear cropped plates.
* Accuracy improvements by:

  * Resizing and enhancing plate images.
  * Using grayscale or binary thresholding.
  * Post-processing to correct common OCR mistakes:
    (`O ↔ 0`, `S ↔ 5`, `I ↔ 1`, `G ↔ 6`, etc.)

---

## 💼 Real-world Applications

* Automated entry/exit systems in parking lots.
* Traffic camera plate reading.
* Vehicle tracking in smart cities.

---

## 👤 Author

* **Name**: Do Tuan Minh
* **Role**: AI student & developer of this pipeline and interface
* **GitHub**: [github.com/your-username](https://github.com/your-username)

---

## ⭐ Like this project?

If you find this helpful, consider giving it a **⭐ Star** to support the work!

---

```

---

👉 Bạn chỉ cần thay:
- `github.com/your-username` bằng link GitHub của bạn.
- `test_images/sample1.jpg` bằng ảnh thật trong thư mục ảnh của bạn.
- `https://user-images.githubusercontent.com/placeholder/plate-demo.gif` bằng demo thật (nếu có GIF/ảnh).

Nếu cần mình tạo **demo GIF đẹp**, mình có thể giúp bạn thêm phần đó luôn.
```
