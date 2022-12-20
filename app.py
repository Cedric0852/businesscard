import streamlit as st
import pytesseract
from PIL import Image
import os
import re
import csv

st.title('OCR Tool FOR BUSINESS CARD V1.0 ')

uploaded_file = st.file_uploader("Choose Business card image file", type=["jpg", "png"])

def extract_text_from_image(image):
    # Extract the text from the image
    text = pytesseract.image_to_string(image)
    return text
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)

    # Extract the text from the image
    text = extract_text_from_image(image)

    # Display the extracted text
    st.image(uploaded_file, caption="Uploaded image", use_column_width=True)
    st.write(text)
    # Add a text area widget to allow the user to edit the extracted text
    edited_text = st.text_area("Edit the extracted text:", value=text)
if st.button("Save"):
    # Save the edited text to a file
    with open("edited_text.txt", "w") as f:
        f.write(edited_text)
    st.success("Text saved to file!")


