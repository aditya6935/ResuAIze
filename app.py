from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
from prompts import input_prompt1, input_prompt3, input_prompt4, input_prompt5
from ocr_utils import extract_text_from_image, grammar_and_spelling_check

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini response function
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# PDF to image + Base64 conversion
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts, first_page
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App
st.set_page_config(page_title="ResuAIze")
st.header("ResuAIze")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")
submit4 = st.button("Skill Gap Learning Plan")
submit5 = st.button("Grammar & Spelling Check")

# Resume Review
if submit1:
    if uploaded_file:
        pdf_content, _ = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Percentage Match
elif submit3:
    if uploaded_file:
        pdf_content, _ = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Skill Gap Analysis
elif submit4:
    if uploaded_file:
        pdf_content, _ = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("🎓 Skill Gap Learning Plan")
        st.write(response)
    else:
        st.write("Please upload the resume")

# OCR + Grammar Check
elif submit5:
    if uploaded_file:
        pdf_content, first_page_image = input_pdf_setup(uploaded_file)
        extracted_text = extract_text_from_image(first_page_image)
        st.subheader("Extracted Resume Text")
        st.write(extracted_text)

        corrections = grammar_and_spelling_check(extracted_text)
        if corrections:
            st.subheader("🚩 Grammar & Spelling Issues Found")
            for correction in corrections:
                st.markdown(f"**Issue:** {correction['issue']}")
                st.markdown(f"**Suggestion:** {', '.join(correction['suggestion'])}")
                st.markdown(f"**Context:** {correction['context']}")
                st.markdown("---")
        else:
            st.success("No Grammar or Spelling Errors Found!")
    else:
        st.write("Please upload the resume")
