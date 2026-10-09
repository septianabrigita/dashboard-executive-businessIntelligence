import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Config Halaman
st.set_page_config(
    page_title="Executive BI Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    csv_path = 'latihan1.csv'
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        np.random.seed(42)
        n = 100
        df = pd.DataFrame({
            'Student_ID': [f'STD-{1001 + i}' for i in range(n)],
            'Gender': np.random.choice(['F', 'M'], size=n),
            'Age': np.random.randint(18, 25, size=n),
            'Study_Hours': np.round(np.random.uniform(1.0, 10.0, size=n), 1),
            'Sleep_Hours': np.round(np.random.uniform(4.0, 9.0, size=n), 1),
            'Attendance': np.round(np.random.uniform(60.0, 100.0, size=n), 1),
            'Exam_Score': np.round(np.random.uniform(50.0, 100.0, size=n), 1),
            'Monthly_Spending': np.round(np.random.uniform(500, 3500, size=n), 0),
            'Screen_Hours': np.round(np.random.uniform(2.0, 12.0, size=n), 1),
            'Satisfaction': np.random.randint(1, 6, size=n)
        })
    return df

df = load_data()

# Layout Dashboard
st.title("📊 Executive BI Dashboard & Predictive Analytics")

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Rata-rata Nilai Ujian", f"{df['Exam_Score'].mean():.1f}")
col2.metric("Rata-rata Jam Belajar", f"{df['Study_Hours'].mean():.1f} Jam")
col3.metric("Rata-rata Kehadiran", f"{df['Attendance'].mean():.1f}%")

st.markdown("---")

# Visualisasi
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Hubungan Jam Belajar vs Nilai Ujian")
    fig_scatter = px.scatter(df, x="Study_Hours", y="Exam_Score", color="Gender", template="plotly_dark")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_right:
    st.subheader("Distribusi Nilai Ujian")
    fig_hist = px.histogram(df, x="Exam_Score", nbins=15, template="plotly_dark")
    st.plotly_chart(fig_hist, use_container_width=True)

st.subheader("📑 Data Student Records")
st.dataframe(df, use_container_width=True)
