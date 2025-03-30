import streamlit as st

# Load index.html as a string
def load_html():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

# Streamlit App
st.set_page_config(page_title="Student Spot", layout="wide")

st.markdown("<h1 style='text-align: center; color: #ff6600;'>Student Spot</h1>", unsafe_allow_html=True)

# Embed the HTML content inside Streamlit
st.components.v1.html(load_html(), height=1000, scrolling=True)
