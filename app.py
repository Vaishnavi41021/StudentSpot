import streamlit as st

# Set page title
st.set_page_config(page_title="Student Spot", layout="wide")

# Load images using Streamlit
st.title("Welcome to Student Spot")
st.write("Empowering Students, Elevating Futures")

# Display the logo
st.image("logo.png", width=200)

# Slideshow (Manual method)
st.image(["banner 1.png", "banner 2.png", "banner 3.png"], 
         caption=["Banner 1", "Banner 2", "Banner 3"], use_container_width=True)

# Services Section
st.header("Our Services")
st.image(["TSS (1).jpg", "TSS (2).jpg", "TSS (3).jpg","TSS (4).jpg","TSS (5).jpg","TSS (6).jpg","TSS (7).jpg","TSS (8).jpg","TSS (9).jpg","TSS (10).jpg"], width=200)

# Contact Section
st.header("Contact Us")
st.write("📧 Email: thestudentspotofficial@gmail.com")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("instagram.png", width=40)
    st.write("Instagram: @the_studentspot")
with col2:
    st.image("linkedin.png", width=40)
    st.write("LinkedIn: The Student Spot")
with col3:
    st.image("whatsapp.png", width=40)
    st.write("WhatsApp: 9581929676")
