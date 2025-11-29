# ---------------------------------------------------------
# FIXED WEATHER APP (NO API KEY NEEDED)
# Developer's Arena Internship - Week 6
# ---------------------------------------------------------

import requests
from datetime import datetime

BASE_URL = "https://wttr.in/"

def get_weather(city):
    try:
        city = city.strip().replace(" ", "+")   # clean city name
        url = f"{BASE_URL}{city}?format=j1"

        response = requests.get(url)
        data = response.json()

        # Extract weather details
        current = data["current_condition"][0]
        temp = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n===== WEATHER REPORT =====")
        print("City:", city.replace("+", " ").title())
        print("Time:", time_now)
        print("Temperature:", temp, "°C")
        print("Condition:", desc)
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind, "km/h")
        print("==========================\n")

    except requests.exceptions.ConnectionError:
        print("⚠ No internet connection!")
    except Exception as e:
        print("Unexpected Error:", e)


def main():
    print("=== WEATHER APP (NO API KEY NEEDED) ===")

    while True:
        city = input("Enter city name (or 'exit'): ")

        if city.lower() == "exit":
            print("Exiting weather application...")
            break

        get_weather(city)


if __name__ == "__main__":
    main()
