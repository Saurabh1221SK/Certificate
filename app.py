import streamlit as st
import os
from PIL import Image
import fitz

# Title of the app
st.title("Certificate Showcase")

# Path to the folder containing certificates
CERTIFICATE_FOLDER = "certificates"

# Function to display images
def display_image(file_path):
    image = Image.open(file_path)
    st.image(image, caption=os.path.basename(file_path), use_container_width=True)  
# Function to display PDFs
def display_pdf(file_path):
    pdf = fitz.open(file_path)
    for page_num in range(pdf.page_count):
        page = pdf[page_num]
        pix = page.get_pixmap()
        st.image(pix.tobytes(), caption=f"{os.path.basename(file_path)} - Page {page_num + 1}", use_container_width=True)  # updated parameter

# Fetching all files from the certificates folder
certificates = [f for f in os.listdir(CERTIFICATE_FOLDER) if os.path.isfile(os.path.join(CERTIFICATE_FOLDER, f))]

# Displaying certificates one by one
for certificate in certificates:
    file_path = os.path.join(CERTIFICATE_FOLDER, certificate)
    file_extension = os.path.splitext(certificate)[1].lower()

    st.write(f"### {certificate}")

    # Checking file type and display accordingly
    if file_extension in [".png", ".jpg", ".jpeg"]:
        display_image(file_path)
    elif file_extension == ".pdf":
        display_pdf(file_path)
    else:
        st.write(f"Unsupported file format: {file_extension}")

    st.write("---")  