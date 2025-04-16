import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

CSV_PATH = Path("pollen_counts.csv")

# Load existing data if file exists
if CSV_PATH.exists():
    df = pd.read_csv(CSV_PATH)
else:
    df = pd.DataFrame(columns=["date", "count"])

url = 'https://www.atlantaallergy.com/pollen_counts'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

span = soup.find('span', class_="pollen-num")
count = span.get_text(strip=True)

heading = span.find_previous('h3').get_text(strip=True)
date = heading.split(' ')[-1].split(':')[0]

# Check last 10 entries for duplicate date
if not (df.tail(10)['date'] == date).any():
    new_row = pd.DataFrame([{"date": date, "count": count}])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)
    print(f"Added new entry: {date} - {count}")
else:
    print(f"Date {date} already exists in recent entries, skipping.")
