import schedule
import time
import subprocess

def run_pipeline():
    print("Running Weather Pipeline...")

    subprocess.run([
        r"C:\Users\saide\projects\weather-data-pipeline\venv\Scripts\python.exe",
        r"C:\Users\saide\projects\weather-data-pipeline\weather_pipeline.py"
    ])

schedule.every(5).minutes.do(run_pipeline)

print("Scheduler started... running every 5 minutes")

while True:
    schedule.run_pending()
    time.sleep(1)