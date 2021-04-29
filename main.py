from config import *
import pandas as pd
from datetime import datetime
from random import randint
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if (today_tuple in birthday_dict):
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"

    with open(file_path, mode="r") as letter_file:
        contents = letter_file.read()
        contents = contents.replace(PLACEHOLDER, birthday_person["name"])

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Til Hamingju Med Afmaelid!\n\n{contents}")
