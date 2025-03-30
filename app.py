import streamlit as st

# Set page title
st.set_page_config(page_title="Student Spot", layout="wide")

# Load images using Streamlit
st.title("Welcome to Student Spot")
st.write("Empowering Students, Elevating Futures")

# Display the logo
st.image("images/logo.png", width=200)

# Slideshow (Manual method)
st.image(["images/banner_1.png", "images/banner_2.png", "images/banner_3.png"], 
         caption=["Banner 1", "Banner 2", "Banner 3"], use_column_width=True)

# Services Section
st.header("Our Services")
st.image(["images/TSS (1).jpg", "images/TSS (2).jpg", "images/TSS (3).jpg"], width=200)

# Contact Section
st.header("Contact Us")
st.write("📧 Email: thestudentspotofficial@gmail.com")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/instagram.png", width=40)
    st.write("Instagram: @the_studentspot")
with col2:
    st.image("images/linkedin.png", width=40)
    st.write("LinkedIn: The Student Spot")
with col3:
    st.image("images/whatsapp.png", width=40)
    st.write("WhatsApp: 9581929676")
