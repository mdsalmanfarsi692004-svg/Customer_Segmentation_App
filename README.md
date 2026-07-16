
``markdown
# ⚡ Enterprise Customer Segmentation AI

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enterprise-customer-segmentation.streamlit.app)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade **AI Analytics & Customer Segmentation Web Platform** built using **Python, Scikit-Learn, and Streamlit**. 

This application leverages unsupervised Machine Learning (**K-Means Clustering**) to analyze customer demographic data and purchasing behaviors in real-time. It allows businesses and marketing teams to dynamically segment customers, personalize engagement strategies, and optimize Customer Relationship Management (CRM) workflows.

---

## 🚀 Live Demo

Experience the interactive dashboard in real-time:  
👉 **[Launch Enterprise Customer Segmentation Hub](https://enterprise-customer-segmentation.streamlit.app)**

---

## ✨ Key Features

* **⚡ Real-Time Analytics Dashboard:** Built with a sleek, responsive, and wide-layout Streamlit interface designed for executive presentations and rapid decision-making.
* **🤖 Unsupervised ML Engine:** Utilizes a pre-trained K-Means clustering algorithm to group customers into distinct behavioral segments instantly.
* **📐 Automated Feature Scaling:** Dynamically standardizes input metrics using a serialized `StandardScaler` pipeline to maintain zero mean and unit variance across all features.
* **🛡️ Modular & Production-Ready Architecture:** Clean separation of concerns between exploratory data analysis/model training (`Analysis_Model.ipynb`) and real-time inference (`Segmentation.py`).

---

## 🧠 Machine Learning Architecture

The segmentation engine processes behavioral and financial metrics through a standardized two-stage pipeline:
1. **Data Preprocessing & Normalization:** Continuous variables with varying scales (e.g., Annual Income vs. Web Visits) are normalized using **`StandardScaler`** (`scaler.pkl`) to prevent features with larger magnitudes from dominating the distance calculations.
2. **Clustering Algorithm:** A pre-trained **K-Means Clustering** model (`kmeans_model.pkl`) assigns the normalized feature vectors to optimal centroids, minimizing within-cluster sum-of-squares (inertia) to define clear customer personas.

---

## 📂 Repository Structure

``text
├── Analysis_Model.ipynb       # EDA, Feature Engineering & K-Means Model Development
├── Segmentation.py            # Main Streamlit Enterprise Dashboard Application
├── customer_segmentation.csv  # Historical Dataset used for Model Training
├── kmeans_model.pkl           # Pre-trained K-Means Clustering Model
├── scaler.pkl                 # Pre-trained StandardScaler for Real-time Inference
├── requirements.txt           # Project Dependencies & Environment Configuration
├── Screenshot - 1.jpeg        # Dashboard UI Snapshot 1
├── Screenshot - 2.jpeg        # Dashboard UI Snapshot 2
├── Screenshot - 3.jpeg        # Dashboard UI Snapshot 3
└── README.md                  # Project Documentation

```

---

## 🖥️ Interactive App Parameters

The application segments customers based on **7 critical demographic and behavioral parameters**:

| Parameter | Category | Range / Unit | Description |
| --- | --- | --- | --- |
| **Age** | Demographic | 18 – 100 Years | The customer's current age. |
| **Annual Income** | Financial | $0 – $200,000 | Total yearly household income of the customer. |
| **Total Spending** | Behavioral | $0 – $5,000 | Cumulative monetary spending across all product categories. |
| **Web Purchases** | Channel | 0 – 100 Transactions | Total number of purchases completed via the online portal. |
| **Store Purchases** | Channel | 0 – 100 Transactions | Total number of purchases made in physical retail stores. |
| **Monthly Web Visits** | Engagement | 0 – 50 Visits | Average number of visits to the online store per month. |
| **Recency** | Loyalty | 0 – 365 Days | Elapsed days since the customer's most recent purchase. |

---

## ▶️ Local Installation & Setup

Follow these steps to deploy and run the dashboard locally on your machine:

### 1. Clone the Repository

Open your terminal or command prompt and clone the project:

```bash
git clone [https://github.com/mdsalmanfarsi692004-svg/Customer_Segmentation_App.git](https://github.com/mdsalmanfarsi692004-svg/Customer_Segmentation_App.git)
cd Customer_Segmentation_App

```

### 2. Create a Virtual Environment (Recommended)

Create an isolated environment to prevent dependency conflicts:

```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

Install all required libraries using the provided requirements file:

```bash
pip install -r requirements.txt

```

### 4. Launch the Streamlit Application

Start the local server to run the app:

```bash
streamlit run Segmentation.py

```

*The dashboard will automatically open in your default web browser at `http://localhost:8501`.*

---

## 📸 Platform Screenshots

### 📊 Executive Dashboard & Demographic Inputs

### 💳 Behavioral & Channel Metrics

### 🤖 Real-Time AI Recommendation Engine Output

---

## 🛠️ Technologies & Tools Used

* **Core Programming:** Python 3.13+
* **Machine Learning & Math:** Scikit-Learn, NumPy
* **Data Manipulation:** Pandas
* **Frontend Dashboard:** Streamlit
* **Model Serialization:** Joblib
* **Version Control & Deployment:** Git, GitHub, Streamlit Cloud

---

## 📌 Future Roadmap

* [ ] **3D Interactive Visualizations:** Integrate Plotly to render 3D PCA/t-SNE cluster distribution charts directly on the dashboard.
* [ ] **Automated PDF Reporting:** Allow marketing teams to download automated executive summary PDFs for each predicted cluster.
* [ ] **Generative AI Persona Integration:** Implement an LLM API to generate natural language explanations and marketing copy for predicted segments.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

If you have suggestions for improving this platform, feel free to open an issue or submit a pull request:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author & Contact

**Md Salman Farsi**

*Aspiring Data Analyst & AI/ML Engineer*

* 🌐 **LinkedIn:** [Connect with me on LinkedIn](https://www.linkedin.com/in/md-salman-farsi-5a609737b)
* 💻 **GitHub Profile:** [@mdsalmanfarsi692004-svg](https://www.google.com/search?q=https://github.com/mdsalmanfarsi692004-svg)

---
