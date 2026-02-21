import streamlit as st
import pandas as pd
import json

from extractor import extract_text_from_pdf, extract_text_from_docx
from utils import clean_text
from parser import parse_resume

st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:

    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    text = clean_text(text)
    result = parse_resume(text)

    st.subheader("Extracted Information")
    st.json(result)

    df = pd.DataFrame([result])

    st.download_button(
        "Download JSON",
        json.dumps(result, indent=4),
        file_name="parsed_resume.json"
    )

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        file_name="parsed_resume.csv"
    )