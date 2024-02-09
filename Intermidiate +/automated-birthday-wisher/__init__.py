import datetime as dt
import smtplib
import pandas

now = dt.datetime.today()
today = (now.month, now.day)

my_email = "codegeek3813@gmail.com"
app_password = "nmwnvbeajzhyvowa"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["Month"], data_row["Day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:

    birthday_person = birthdays_dict[today]
    name = birthday_person["Name"]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        # Secure the email and encrypt the data
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="mdheraj0403@gmail.com",
                            msg=f"Subject: Happy Birthday!\n\nDear {name},\n\nWishing you a day filled with joy, laughter, and all the things that make you happiest!\nCheers to another amazing year ahead. Happy birthday!\n\nBest Regards from,\nDheraj M")
