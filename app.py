import streamlit as st
from PIL import Image, ImageFilter
import io

# Set up the title and introduction of the app
st.title('IMAGE2PIXELART')
st.subheader('🎨 Convert any PNG/JPG/JPEG images into pixel art with filters.')
st.caption('Upload your image, apply filters, and then convert it into pixel art.')

# File uploader to allow users to upload their image
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open and display the original image
    img = Image.open(uploaded_file)
    st.image(img, caption='Original Image', width=400)

    # Filter options
    filter_option = st.selectbox("Select a filter to apply:",
                                 ["None", "Grayscale", "Blur", "Contour", "Edge Enhance", "Emboss"])
    
    # Apply selected filter
    if filter_option == "Grayscale":
        img = img.convert("L")
    elif filter_option == "Blur":
        img = img.filter(ImageFilter.BLUR)
    elif filter_option == "Contour":
        img = img.filter(ImageFilter.CONTOUR)
    elif filter_option == "Edge Enhance":
        img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_option == "Emboss":
        img = img.filter(ImageFilter.EMBOSS)

    # Show filtered image
    st.image(img, caption='Filtered Image', width=400)

    # Sliders for user input on colors and grid size
    colors = st.slider('Number of colors to use', 1, 256, 100)
    grid_size = st.slider('Grid size (in pixels)', 1, min(img.size), 50)

    # Processing image to create pixel art
    img = img.convert('P', palette=Image.ADAPTIVE, colors=colors)
    img = img.resize((grid_size, int(grid_size * img.height / img.width)), Image.NEAREST)
    pixel_art = img.resize((500, int(500 * img.height / img.width)), Image.NEAREST)

    # Display the pixel art
    st.image(pixel_art, caption='Pixel Art Output', width=400)

    # Allow users to download the pixel art
    buf = io.BytesIO()
    pixel_art.save(buf, format="PNG")
    byte = buf.getvalue()
    st.download_button(label="Download Pixel Art", data=byte, file_name="pixel_art.png", mime="image/png")

# Additional information and instructions
st.sidebar.header("Instructions")
st.sidebar.text("1. Upload your image.\n"
                "2. Choose a filter.\n"
                "3. Adjust the settings.\n"
                "4. View and download the result.")

# About section
st.sidebar.header("About")
st.sidebar.info("This app is created to demonstrate how images can be transformed into pixel art using Python and Streamlit. Filters can enhance the artistic effect before pixelation.")
