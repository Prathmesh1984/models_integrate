import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Crop Recommendation", layout="wide")

# --------------------
# Load dataset
# --------------------
@st.cache_data
def load_recommendation_data():
    return pd.read_csv("5ab347f9-bb42-4cd4-96ac-c2a26cf8c659.csv")

df = load_recommendation_data()

# --------------------
# Train Model
# --------------------
X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# --------------------
# UI
# --------------------
st.markdown(
    "<h2 style='text-align: center; color: green;'>🌱 Crop Recommendation System</h2>",
    unsafe_allow_html=True,
)
st.write("Enter soil and climate details to get the best crop suggestion.")

N = st.number_input("Nitrogen", min_value=0, max_value=140)
P = st.number_input("Phosphorus", min_value=5, max_value=145)
K = st.number_input("Potassium", min_value=5, max_value=205)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0)
humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0)
ph = st.number_input("Soil pH", min_value=3.5, max_value=9.5)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0)

if st.button("Predict Crop"):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    result = model.predict(input_data)
    st.success(f"✅ Recommended Crop: **{result[0]}**")
