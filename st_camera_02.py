import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io
import pandas as pd

st.title("📸 Camera")

# --- Capture ---
img_file = st.camera_input("Take a photo")

if img_file is not None:

    # ── Display original ──────────────────────────────────────────
    st.subheader("Original")
    st.image(img_file, use_container_width=True)


