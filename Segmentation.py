import streamlit as st
import pandas as pd
import numpy as np
import joblib

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="AI Customer Segmentation Hub",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Enterprise-Grade Dark Theme & Polish
st.markdown("""
    <style>
    /* Main Dashboard Header */
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FAFAFA;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #8E9297;
        margin-bottom: 30px;
    }
    /* Section Headers */
    .section-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #007BFF;
        margin-top: 10px;
        margin-bottom: 15px;
        border-bottom: 2px solid #1E2130;
        padding-bottom: 5px;
    }
    /* Custom Card Styling for Prediction Result */
    .result-card {
        background: linear-gradient(135deg, #1E2130 0%, #0E1117 100%);
        border: 1px solid #007BFF;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 123, 255, 0.15);
        margin-top: 20px;
    }
    .result-title {
        color: #8E9297;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }
    .result-value {
        color: #00E676;
        font-size: 2.2rem;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Load ML Models safely
@st.cache_resource
def load_models():
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return kmeans, scaler

try:
    kmeans, scaler = load_models()
except Exception as e:
    st.error(f"⚠️ Error loading models: {e}. Please ensure 'kmeans_model.pkl' and 'scaler.pkl' are in the directory.")
    st.stop()

# 4. Header Section
st.markdown('<p class="main-title">👥 AI Customer Segmentation Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Enter customer behavioral & demographic data below to generate real-time segmentation analytics.</p>', unsafe_allow_html=True)

st.write("---")

# 5. Modular 3-Column Layout for Form Inputs
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown('<p class="section-header">🧑 Demographic Profile</p>', unsafe_allow_html=True)
    age = st.number_input("Age (Years)", min_value=18, max_value=100, value=35, step=1, help="Customer's current age.")
    income = st.number_input("Annual Income ($)", min_value=0, max_value=200000, value=50000, step=1000, help="Total yearly household income.")

with col2:
    st.markdown('<p class="section-header">💳 Financial & Loyalty Metrics</p>', unsafe_allow_html=True)
    total_spending = st.number_input("Total Spending ($)", min_value=0, max_value=5000, value=1000, step=50, help="Sum of purchases across all categories.")
    recency = st.number_input("Recency (Days)", min_value=0, max_value=365, value=30, step=1, help="Days elapsed since the last purchase.")

with col3:
    st.markdown('<p class="section-header">🛒 Engagement & Channels</p>', unsafe_allow_html=True)
    num_web_purchases = st.number_input("Web Purchases", min_value=0, max_value=100, value=10, step=1, help="Total transactions made via online store.")
    num_store_purchases = st.number_input("Store Purchases", min_value=0, max_value=100, value=10, step=1, help="Total transactions made in physical stores.")
    num_web_visits = st.number_input("Monthly Web Visits", min_value=0, max_value=50, value=3, step=1, help="Average visits to the online portal per month.")

st.write("---")

# 6. Data Preprocessing & Prediction Action
input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

# Center align the button using columns
btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])

with btn_col2:
    predict_clicked = st.button("⚡ Run Segmentation AI", use_container_width=True, type="primary")

if predict_clicked:
    with st.spinner("🤖 Analyzing customer features using K-Means clustering..."):
        # Scale the inputs
        input_scaled = scaler.transform(input_data)
        # Generate Prediction
        cluster = kmeans.predict(input_scaled)[0]

    # 7. Sleek Executive Result Card
    st.markdown(f"""
        <div class="result-card">
            <div class="result-title">AI Recommendation Engine Output</div>
            <div class="result-value">Assigned to Segment: Cluster {cluster}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Optional: Display a summary profile matrix
    st.caption("📊 Customer Profile Snapshot:")
    st.dataframe(input_data, use_container_width=True, hide_index=True)
