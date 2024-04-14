import streamlit as st
from PIL import Image
import os

from src.main import pipeline

# Define paths to example images
EXAMPLE_IMAGE_PATHS = {
    "Tiger": "dominant-colors/images/tiger.jpg",
    "Flowers": "dominant-colors/images/flowers.jpeg",
    "Mountains": "dominant-colors/images/mountains.jpeg"
}

# Function to display the dominant colors pipeline
def display_dominant_colors(image, image_path):
    st.image(image, use_column_width=True)
    pipeline(image_path)
    st.image('dominant_colors.png', caption='Dominant Colors', use_column_width=True)

def main():

    # Streamlit setup
    st.title("Display Dominant Colors")
    st.markdown("""
        <style>
        [data-testid ="stHeading"] {
        margin-top: -75px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Sidebar setup
    st.sidebar.title("Upload a picture")
    
    # File uploader for user-uploaded images
    uploaded_file = st.sidebar.file_uploader("Upload your own image", type=["jpg", "webp", "jpeg"])

    # Selectbox for example images
    selected_image = st.sidebar.selectbox("Or choose a sample image:", list(EXAMPLE_IMAGE_PATHS.keys()))
    use_sample_images = st.sidebar.checkbox("Use sample image", value=False)

    if uploaded_file is not None and use_sample_images is True:
        st.warning('Please remove the uploaded photo or deselect the "Use sample image" checkbox')
    elif uploaded_file is not None and use_sample_images is False:
        # Process the uploaded file
        display_dominant_colors(uploaded_file, uploaded_file)
    elif use_sample_images is True:
        # Process the selected example image
        image_path = EXAMPLE_IMAGE_PATHS[selected_image]
        image = Image.open(image_path)
        display_dominant_colors(image, image_path)

if __name__ == "__main__":
    main()