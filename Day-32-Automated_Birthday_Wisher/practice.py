# import smtplib
#
# my_email = "rakinudemy@gmail.com"
# password = "ffnfxonbgemldmnp"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rakinudemy@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )

import datetime as dt
import random
import smtplib
now = dt.datetime.now()
weekday = now.weekday()

my_email = "rakinudemy@gmail.com"
password = "ffnfxonbgemldmnp"

if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rakinudemy@yahoo.com",
            msg=f"Subject:Quote of the day.\n\n{quote}"
        )
