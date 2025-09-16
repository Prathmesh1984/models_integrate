import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Crop Yield Prediction", layout="wide")

# --------------------
# Load dataset
# --------------------
@st.cache_data
def load_data():
    return pd.read_csv("india_crop_yield_dataset.csv")

df = load_data()

# --------------------
# Title
# --------------------
st.markdown(
    "<h2 style='text-align: center; color: green;'>📈 Farmer Friendly Crop Yield Prediction</h2>",
    unsafe_allow_html=True,
)
st.write("Enter details below to predict your crop yield (tonnes per hectare).")

# --------------------
# Preprocessing
# --------------------
target = "Yield_t_per_ha"
X = df.drop(columns=[target, "Sowing_date", "Harvest_date", "Production_tonnes", "Year"])
y = df[target]

categorical_cols = X.select_dtypes(include=["object"]).columns
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# --------------------
# Input Form
# --------------------
st.subheader("📝 Fill in Crop & Field Details")

cols = st.columns(3)
input_data = {}

for i, col in enumerate(X.columns):
    with cols[i % 3]:
        if col in categorical_cols:
            options = list(encoders[col].classes_)
            if col == "District":
                choice = st.select_slider("District", options=options)
            else:
                choice = st.selectbox(col, options)
            input_data[col] = encoders[col].transform([choice])[0]
        else:
            val = st.number_input(
                col,
                float(X[col].min()),
                float(X[col].max()),
                float(X[col].mean()),
            )
            input_data[col] = val

# --------------------
# Prediction
# --------------------
st.markdown("---")
if st.button("🌱 Predict Yield"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    st.success(f"✅ Your predicted crop yield is: **{prediction:.2f} tonnes per hectare**")

# --------------------
# Show Model Accuracy
# --------------------
score = model.score(X_test, y_test)
st.markdown("### 📊 Model Performance")
st.metric("R² Score on Test Data", f"{score:.2f}")
