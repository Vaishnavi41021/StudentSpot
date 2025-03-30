import streamlit as st

st.set_page_config(page_title="Student Spot", layout="wide")

# Use Streamlit to load images
st.image("images/logo.png", width=250)

# Slideshow (Manual method)
st.image(["images/banner 2.png", "images/banner 3.png", "images/banner img 1.png"], caption=["Banner 2", "Banner 3", "Banner 1"], use_column_width=True)

# Contact Section with Images
st.subheader("Contact Us")
st.write("📧 Email: thestudentspotofficial@gmail.com")
st.image("images/instagram.png", width=40)
st.write("Instagram: the_studentspot")
st.image("images/linkedin.png", width=40)
st.write("LinkedIn: The Student Spot")
