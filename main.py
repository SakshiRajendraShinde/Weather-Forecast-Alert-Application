import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# User input
city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("message"))
        exit()

    # Extract weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n===== WEATHER REPORT =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather}")
    print(f"Wind Speed: {wind_speed} m/s")

    # Alerts
    alerts = []

    if temperature > 35:
        alerts.append("🔥 High Temperature Alert!")

    if humidity > 85:
        alerts.append("💧 High Humidity Alert!")

    if "rain" in weather.lower():
        alerts.append("🌧 Rain Alert!")

    if "storm" in weather.lower():
        alerts.append("⛈ Storm Alert!")

    print("\n===== ALERTS =====")

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No weather alerts.")

    # Save report
    report = {
        "Date": [datetime.now()],
        "City": [city],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Weather": [weather],
        "Wind Speed": [wind_speed]
    }

    df = pd.DataFrame(report)

    os.makedirs("reports", exist_ok=True)

    file_name = f"reports/{city}_weather_report.csv"

    df.to_csv(file_name, index=False)

    print(f"\nReport saved: {file_name}")

    # Visualization
    plt.figure(figsize=(6, 4))
    plt.bar(["Temperature", "Humidity"], [temperature, humidity])

    plt.title(f"Weather Analysis - {city}")
    plt.ylabel("Values")

    os.makedirs("outputs", exist_ok=True)

    chart_path = f"outputs/{city}_chart.png"

    plt.savefig(chart_path)

    print(f"Chart saved: {chart_path}")

    plt.show()

except Exception as e:
    print("Error occurred:", e)