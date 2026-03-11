import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤",
    layout="wide"
)

st.title("☁️ Weather Data Dashboard")

engine = create_engine("postgresql://postgres:12345@localhost:5432/weather_db")

query = "SELECT * FROM weather_data ORDER BY timestamp DESC"

df = pd.read_sql(query, engine)

latest = df.iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Current Temperature (°C)", latest["temperature"])
col2.metric("Humidity (%)", latest["humidity"])
col3.metric("Weather", latest["weather"])

st.divider()

st.subheader("Latest Weather Data")
st.dataframe(df)

st.subheader("Temperature Trend")

df["timestamp"] = pd.to_datetime(df["timestamp"])

st.line_chart(df.set_index("timestamp")["temperature"])