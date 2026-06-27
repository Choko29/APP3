# app3_summary.py
import os
import streamlit as st
import teacher_summary
from config import DB_PATH

st.set_page_config(page_title="Document Summarizer", page_icon="📝")
st.title("📝 დოკუმენტის ავტომატური Summary")

st.write("დააჭირეთ ღილაკს დოკუმენტის მოკლე შეჯამების მისაღებად.")

if st.button("Summary-ს შექმნა"):
    if os.path.exists(DB_PATH):
        with st.spinner("Summary მზადდება..."):
            summary = teacher_summary.create_summary()
            st.success(summary)
    else:
        st.error("ჯერ შექმენით ბაზა ბრძანებით: python ingest.py")
