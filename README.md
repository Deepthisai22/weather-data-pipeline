### Weather Data Pipeline

## Overview

This project is a simple data pipeline that collects weather data from the OpenWeather API. The data is fetched using Python, processed, and stored in a PostgreSQL database.
The pipeline is automated using a scheduler that runs every 5 minutes to collect updated weather data.

## Architecture

Weather API → python Script -> Data Handling -> storage (postgresql)

The pipeline fetches weather information such as temperature, humidity, pressure, weather condition, and wind speed, and stores it in the database with a timestamp.


## Technologies Used

->OpenWeather API
->python
->Requests
->Pandas
->PostgreSQL
->SQLAlchemy
->Schedule
->Logging

## Schema Design

Weather data is stored in the weather_data table.

Columns:

city
temperature
humidity
pressure
weather
wind_speed
timestamp

Each pipeline run inserts a new record with the latest weather data.

## Running the Pipeline

1. Install dependencies:
   pip install -r requirements.txt

2. Run the scheduler:
   python scheduler.py

The pipeline will run every 5 minutes and store weather data in the PostgreSQL database.

## Features

- Fetches weather data every 5 minutes
- Stores historical weather data
- Shows temperature trend over time

## Conclusion

This project demonstrates a basic automated data pipeline that collects weather data from an API, processes it using Python, and stores the data in PostgreSQL for future analysis.