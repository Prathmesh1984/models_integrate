import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Multi Prediction System for Farmers",
    page_icon="🌾",
    layout="wide"
)

# ----------------------------
# Title Section
# ----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: green;'>
        🌐 Multi Prediction System for Farmers 🌐
    </h1>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Add Image (centered)
# ----------------------------
st.markdown("<h3 style='text-align: center;'>Smart Farming Dashboard</h3>", unsafe_allow_html=True)

# ✅ Fix: remove use_container_width
st.image("unnamed.png", width=900)   # You can adjust width as needed

# ----------------------------
# Welcome Text
# ----------------------------
st.write("### 👋 Welcome! Please choose a prediction system from the sidebar or click a button below:")

# ----------------------------
# Buttons for Navigation
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/1_Yield_Prediction.py",
        label="📊 Go to Crop Yield Prediction",
        icon="🌱"
    )

with col2:
    st.page_link(
        "pages/2_Crop_Recommendation.py",
        label="🌾 Go to Crop Recommendation System",
        icon="🌾"
    )

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Developed for Farmers 🚜 | Powered by Machine Learning</p>",
    unsafe_allow_html=True
)
