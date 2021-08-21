import smtplib
import datetime as dt
import random
import pandas

my_email = "xx@gmail.com"
password = "xxx"

birthday_dataframe = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_dataframe.to_dict("records")

datetime_now = dt.datetime.now()
date_now_list = [datetime_now.month, datetime_now.day]


def prepare_letter(email, name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        letter_template = letter.read()
    letter_ready = letter_template.replace("[NAME]", name)
    send_email(email, name, letter_ready)


def send_email(email, name, letter):
    print("email send")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:HAPPY BIRTHDAY!\n\n{letter}")


[prepare_letter(email=row["email"], name=row["name"])
 for row in birthday_dict if date_now_list == [row["month"], row["day"]]]
