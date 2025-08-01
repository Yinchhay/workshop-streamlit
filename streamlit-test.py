import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sidebar
st.sidebar.image("./assets/logo.png", use_column_width=True)
st.sidebar.header("Climate Project")

# Title
st.title("🌍 Climate Data Dashboard")
st.write("A simple dashboard to visualize climate-related metrics.")

# Simulated data (you can replace with real data)
st.subheader("📊 Key Climate Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Temp", "15.3°C", "+0.2°C")
col2.metric("CO₂ Level", "419 ppm", "+2 ppm")
col3.metric("Sea Level", "3.2 mm", "+0.1 mm")

# Line chart example
st.subheader("🌡️ Temperature Over Time")
date_range = pd.date_range(start="2020-01-01", periods=100)
temp_data = np.random.normal(loc=15, scale=1, size=100)

df_temp = pd.DataFrame({
    "Date": date_range,
    "Temperature (°C)": temp_data
})

st.line_chart(df_temp.set_index("Date"))

# User input example
st.subheader("📍 Compare CO₂ Levels by Year")
year = st.slider("Select year", 2000, 2025, 2020)
co2_level = 370 + (year - 2000) * 2  # Example logic

st.write(f"Estimated CO₂ level in {year}: **{co2_level} ppm**")
