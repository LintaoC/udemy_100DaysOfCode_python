import smtplib
import datetime as dt
import random

my_email = "xx@gmail.com"
password = "xx"

with open("quotes.txt") as file:
    quote_list = file.readlines()

quote_random = quote_list[random.randint(0, 101)]

datetime_now = dt.datetime.now()
day_of_week = datetime_now.weekday()

if day_of_week == 5:
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:This is the subject\n\nHi!"
                f"\nToday is Friday, the {day_of_week+1} day of the week.\n"
                f"There is you motivation quote: \n{quote_random}\nBye")
