import streamlit as st
from src.main import pipeline

if __name__ == "__main__":

    st.title("Display Dominant Colors")
    st.markdown("""
        <style>
        [data-testid ="stHeading"] {
        margin-top: -75px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.title("Upload a picture")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["jpg", "webp", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
        pipeline(uploaded_file)
        st.image('dominant_colors.png', caption='Dominant Colors', use_column_width=True)
