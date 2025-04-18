# Pollen Count Scraper

This is a python script to scrape the [atl pollen count](https://www.atlantaallergy.com/pollen_counts)
and send an email with today's count.
It also tracks to a .csv file for historical data. 

## Setup
### Requirements
Install requirements
```bash
pip install -r requirements.txt
```

Also make sure the script is executable:
```bash
chmod +x get-count.py
``` 

### Email
Create a gmail app password and then create a `.env` file based off
the `.env.example` file.

### Schedule
Add this cron-job to run it in the morning (hours in UTC-0):
```bash
*/5 13-17 * * * /root/Projects/pollen-count-scraper/get-count.py
```
