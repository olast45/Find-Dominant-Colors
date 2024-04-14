import streamlit as st

from src.main import pipeline
from PIL import Image


# Example images
example_images = {
    "Tiger": "dominant-colors/images/tiger.jpg",
    "Flowers": "dominant-colors/images/flowers.jpeg",
    "Mountains": "dominant-colors/images/mountains.jpeg"
}

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
    uploaded_file = st.sidebar.file_uploader("Upload your own image", type=["jpg", "webp", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, use_column_width=True)
        pipeline(uploaded_file)
        st.image('dominant_colors.png', caption='Dominant Colors', use_column_width=True)

    # Sidebar selectbox for choosing example images
    selected_image = st.sidebar.selectbox("Or choose a sample image:", list(example_images.keys()))

    # Load selected example image
    if selected_image:
        image = Image.open(example_images[selected_image])
        st.image(image, use_column_width=True)
        pipeline(example_images[selected_image])
        st.image('dominant_colors.png', caption='Dominant Colors', use_column_width=True)
