from config import *
import pandas as pd
from datetime import datetime
from random import randint
import smtplib
from email.mime.text import MIMEText
from email.header import Header

today = datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if (today_tuple in birthday_dict):
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"

    with open(file_path, mode="r", encoding="utf-8") as letter_file:
        contents = letter_file.read()
        content = contents.replace(PLACEHOLDER, birthday_person["name"])
        
        msg = MIMEText(content, 'plain', 'utf-8')
        msg["Subject"] = Header("Til Hamingju Med Afmælið!", 'utf-8')
        msg["From"] = MY_EMAIL
        msg["To"] = birthday_person["email"]

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                msg["From"], msg["To"], msg.as_string())
