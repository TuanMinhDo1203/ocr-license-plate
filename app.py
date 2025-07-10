import streamlit as st
import cv2
import numpy as np
from detect_ocr import detect_and_ocr

st.set_page_config(page_title="OCR Biển Số Xe", page_icon="🚗", layout="centered")
st.markdown("<h1 style='text-align: center; color: #0066cc;'>🚗 Nhận diện biển số xe bằng AI</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Tải ảnh xe cần nhận diện", type=["jpg", "png"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.markdown("### Ảnh gốc")
    st.image(image, channels="BGR", use_container_width=True)

    st.divider()
    st.markdown("### Kết quả nhận diện biển số:")

    results = detect_and_ocr(image)

    if not results:
        st.warning("❌ Không tìm thấy biển số nào trong ảnh.")
    else:
        for i, r in enumerate(results):
            crop = r["crop"]
            text = r["text_cleaned"]

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(crop, caption=f"📷 Crop #{i+1}", use_container_width=True)

            with col2:
                # Hiển thị biển số lớn, rõ ràng
                plate_display = np.ones((100, 400, 3), dtype=np.uint8) * 255
                cv2.putText(plate_display, text, (10, 65), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 0), 4, cv2.LINE_AA)
                st.image(plate_display, caption=f"🔍 Biển số #{i+1}: `{text}`", use_container_width=True)

        st.success(f"✅ Đã phát hiện {len(results)} biển số.")


# import streamlit as st
# import cv2
# import numpy as np
# from detect_ocr import detect_and_ocr

# st.set_page_config(page_title="OCR Biển Số Xe", page_icon="🚗", layout="centered")
# st.markdown("<h1 style='text-align: center; color: #0066cc;'>🚗 Nhận diện biển số xe bằng AI</h1>", unsafe_allow_html=True)

# uploaded_file = st.file_uploader("📤 Tải ảnh xe cần nhận diện", type=["jpg", "png"])

# if uploaded_file:
#     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#     image = cv2.imdecode(file_bytes, 1)

#     st.markdown("### 🖼️ Ảnh gốc")
#     st.image(image, channels="BGR", use_container_width=True)

#     st.divider()
#     st.markdown("### 🧠 Kết quả nhận diện biển số:")

#     results = detect_and_ocr(image)

#     if not results:
#         st.warning("❌ Không tìm thấy biển số nào trong ảnh.")
#     else:
#         for i, r in enumerate(results):
#             crop = r["crop"]
#             text = r["text_cleaned"]

#             col1, col2 = st.columns([1, 2])

#             with col1:
#                 st.image(crop, caption=f"📷 Crop #{i+1}", use_container_width=True)

#             with col2:
#                 # Hiển thị biển số lớn, rõ ràng
#                 plate_display = np.ones((100, 400, 3), dtype=np.uint8) * 255
#                 cv2.putText(plate_display, text, (10, 65), cv2.FONT_HERSHEY_SIMPLEX,
#                             2, (0, 0, 0), 4, cv2.LINE_AA)
#                 st.image(plate_display, caption=f"🔍 Biển số #{i+1}: `{text}`", use_container_width=True)

#         st.success(f"✅ Đã phát hiện {len(results)} biển số.")
