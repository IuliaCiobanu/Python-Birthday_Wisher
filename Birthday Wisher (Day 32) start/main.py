import smtplib
import random

my_email="iulia.codeaza@gmail.com"
my_password="*******"

import datetime as dt
now=dt.datetime.now()
day_of_week=now.weekday()


with open("quotes.txt") as text:
    quotes_list=text.readlines()
    monday_quote=random.choice(quotes_list)
    if day_of_week==5:
        with smtplib.SMTP( "smtp.gmail.com", 587 ) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="caisa.caisata@yahoo.com", msg=f"Subject:Mesaj motivant"
                                                                                           f"\n\n{monday_quote}")

    print(monday_quote)
