import pandas as pd
from datetime import datetime, timedelta
from pandas.io.formats.format import return_docstring
import smtplib 
import time 
import requests 
from win10toast import ToastNotifier 

#your gmail credentials 
gmail_id = "codepersontest@gmail.com"
gmail_password = "Chiomabobo123"

#for desktop notifications 
toast = ToastNotifier()

#define a function for sending the email
def sendemail(to, sub, msg):

    #connection to gmail
    gmail_obj = smtplib.SMTP('smtp.gmail.com',537)

    #starting the session 
    gmail_obj.starttls()

    #login using credentials
    gmail_obj.sendmail(gmail_id, to, 
                        f"Subject : {sub}\n\n{msg}")

    #quit session
    gmail_obj.quit()
    
    # print("Email sent to " + str(to) + "with subject" + str(sub) + " and message :" + str(msg))

    # toast.show_toast("Email Sent!",
    #                 f"{name} was sent e-mail",
    #                 threaded=True,
    #                 icon_path=None,
    #                 duration=6)

    # while toast.notification_active():
    #     time.sleep(0.1)

file = "projectt.xlsx"
data = pd.read_excel(file, sheet_name=0)

def get_due_row() -> list:
    people_to_pay = []
    for row in range(0, len(data)):
        now = datetime.now()
        date = data.iloc[row, 4]
        due = now - date
        if due.days >= 30:
            people_to_pay.append(row)
    return people_to_pay


def msg_to_send(rows):
    msgs = []
    for row in rows:
        person = data.iloc[row, :]
        msg = f"{person['Name']} is due for payment with an outstanding balance of {person['Balance']} of {person['TotalFee']}"
        msgs.append(msg)
    return msgs
