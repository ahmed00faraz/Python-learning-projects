from datetime import datetime
import random
import smtplib
import pandas

EMAIL = "example@gmail.com"
PASSWORD = "yourpassword"


def send_wishes(record):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read().replace("[NAME]", record['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # encrypt ,secure
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="yourTarget@gmail.com",
                                msg=f"Subject:Happy Birthday {record['name']}\n\n" + letter)


now = datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for _ in data:
    if (_['month'], _['day']) == today:
        send_wishes(_)
