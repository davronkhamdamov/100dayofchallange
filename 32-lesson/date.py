import smtplib
from datetime import datetime
import random

my_email = "xamdamovdavron6@gmail.com"
password = ""


with open("32-lesson/quote.txt", "r") as quotes:
    random_quote = random.choice(quotes.readlines())
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs="davronx036@gmail.com",
            msg=f"Subject: Smtp mail send mail test\n\n{random_quote}",
        )
