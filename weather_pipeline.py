import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import logging

# Logging configuration
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "0ab65b26d8a1c89e07f4ab47f204c7c1"
CITY = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now()
    }

    df = pd.DataFrame([weather_data])

    print("Extracted Weather Data:")
    print(df)

    engine = create_engine("postgresql://postgres:12345@localhost:5432/weather_db")

    df.to_sql("weather_data", engine, if_exists="append", index=False)

    logging.info("Weather data inserted successfully")

except Exception as e:
    logging.error(f"Pipeline failed: {e}")
