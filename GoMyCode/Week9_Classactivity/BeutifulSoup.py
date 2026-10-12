import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[1]
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)

# img = tonight.find("img")
# desc = img['title']
# print(desc)


weather_rows = []
for item in forecast_items:
    period_tag = item.find(class_="period-name")
    short_desc_tag = item.find(class_="short-desc")
    temp_tag = item.find(class_="temp")
    img = item.find("img")

    weather_rows.append({
        "period": period_tag.get_text(strip=True) if period_tag else None,
        "short_desc": short_desc_tag.get_text(strip=True) if short_desc_tag else None,
        "temp": temp_tag.get_text(strip=True) if temp_tag else None,
        "desc": (img.get("title") or img.get("alt")) if img else None,
    })

weather = pd.DataFrame(weather_rows)

print(weather)

#Anlaysing our dataframe (Calculating mean,max, min etc)
temp_nums = pd.to_numeric(
    weather["temp"].str.extract(r"(-?\d+)", expand=False), errors="coerce",
).astype('Int64')

print(temp_nums.mean())
print(temp_nums.max())
print(temp_nums.min())
print(temp_nums.std())

# print(soup.prettify())