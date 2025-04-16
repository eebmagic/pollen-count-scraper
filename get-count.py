#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pathlib
import mail

container = pathlib.Path(__file__).parent

# Constants
URL = "https://www.atlantaallergy.com/pollen_counts"
CSV_PATH = container / "pollen_counts.csv"

# Load existing data if file exists
if CSV_PATH.exists():
    df = pd.read_csv(CSV_PATH)
else:
    df = pd.DataFrame(columns=["date", "count"])

# Pull page
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Scan for components
span = soup.find('span', class_="pollen-num")
heading = span.find_previous('h3').get_text(strip=True)

# Parse for data
count = span.get_text(strip=True)
date = heading.split(' ')[-1].split(':')[0]

# Check last 10 entries for duplicate date
if not (df.tail(10)['date'] == date).any():
    # Update the data
    new_row = pd.DataFrame([{"date": date, "count": count}])
    df = pd.concat([df, new_row], ignore_index=True)

    # Write to file
    df.to_csv(CSV_PATH, index=False)
    print(f"Added new entry: {date} - {count}")

    # Send email message
    mail.send(f"Today's pollen count: {count}")
else:
    print(f"Date {date} already exists in recent entries, skipping.")

