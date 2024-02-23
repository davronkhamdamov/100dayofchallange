import smtplib

my_email = "xamdamovdavron6@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs="mynameispro@icloud.com",
        msg="Subject:Hello bro what's up\n\nThis is body of my email",
    )
