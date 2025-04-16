#!/usr/bin/python3

import smtplib
import sys
import os
import pathlib
from dotenv import load_dotenv

# Resolve .env location relative to this script
container = pathlib.Path(__file__).parent
load_dotenv(container / ".env")

msg = None
if len(sys.argv) > 1:
    msg = ' '.join(sys.argv[1:])

# Load credentials and target email from environment variables
gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_APP_PASS")
to = os.getenv("GMAIL_TARGET")

def send(msg):
    text = f"Subject: {msg}\n{msg}"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, text)
        server.close()
    except Exception as e:
        print(e)
        print('Something went wrong...')

