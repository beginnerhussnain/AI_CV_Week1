import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Processing Studio", layout="wide")

st.title("🖼️ Image Processing App")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        
    pil_img = Image.open(uploaded_file)
    img_bgr = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    
    st.sidebar.header("📊 Image Info")
    h, w, c = img_bgr.shape
    st.sidebar.write(f"**Dimensions:** {w} × {h} px")
    st.sidebar.write(f"**Size:** {len(uploaded_file.getvalue()) / 1024:.2f} KB")

    
    mode = st.radio("Choose Operation", ["Original", "Grayscale", "Canny Edge Detection", "Gaussian Blur"])

    if mode == "Original":
        st.image(pil_img, caption="Original Image")
    elif mode == "Grayscale":
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        st.image(gray, caption="Grayscale Image")
    elif mode == "Canny Edge Detection":
        t1 = st.slider("Lower Threshold", 0, 255, 50)
        t2 = st.slider("Upper Threshold", 0, 255, 150)
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, t1, t2)
        st.image(edges, caption="Canny Edges")
    elif mode == "Gaussian Blur":
        k = st.slider("Kernel Size", 1, 31, 5, step=2)
        blur = cv2.GaussianBlur(img_bgr, (k, k), 0)
        st.image(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB), caption="Blurred Image")
else:
    st.info("Please upload an image to begin.")