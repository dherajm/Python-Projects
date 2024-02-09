import datetime as dt
import smtplib
import pandas

now = dt.datetime.today()
today = (now.month, now.day)

my_email = "<EMAIL>"                # Recommended not to use your personal or work email IDs.
app_password = "<APP-PASSWORD>"     # To learn how to obtain an app password for your gamil, watch a youtube video or do some googling.

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["Month"], data_row["Day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    name = birthday_person["Name"]
    receiver_email = birthday_person["Email"]

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject: Happy Birthday!\n\nDear {name},\n\nWishing you a day filled with joy, "
                                f"laughter, and all the things that make you happiest!\nCheers to another amazing "
                                f"year ahead. Happy birthday!\n\nBest Regards from,\n[Your Name]")
