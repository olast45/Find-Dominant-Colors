import streamlit as st
from src.main import pipeline

uploaded_file = st.file_uploader("Choose a file (.jpg, .webp, .jpeg)")
if uploaded_file is not None:
    pipeline(uploaded_file)
    st.image('dominant_colors.png', caption='Dominant Colors', use_column_width=True)
