# automate sending emails from excel with python

#import all the stuff we need 
import pandas as pd 
import time 
import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart


#path of our Excel file as well as all information that we need from that file
# file = "projectt.xlsx"
# openfile = pd.read_excel(file)
# sheet = openfile.sheet_by_name('name')

sheet = pd.read_excel("projectt.xlsx")

mail_list = []
amount = []
name = []
for k in range(sheet.nrows-1):
    name = sheet.cell_value(k+1,0)
    email = sheet.cell_value(k+1,1)
    paid = sheet.cell_value(k+1,2)
    balance = sheet.cell_value(k+1,3)
    
    if paid == 'No': 
        mail_list.append(email)
        amount.append(balance)
        name.append(name)

email = 'codepersontest@gmail.com'
password = 'Chiomabobo123'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)

for mail_to in mail_list:
    send_to_email = mail_to 
    find_des = mail_list.index(send_to_email)
    clientname = name[find_des]
    subject = f'{name} you have a new email'
    message = f'Dear {name}, \n'  \
              f'we inform you that you owe ${amount[find_des]}.  \n'\
              '\n'\
              'Best Regards'

msg = MIMEMultipart()
msg['From'] = send_to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
print(f'Sending email to {clientname}...')
server.sendmail(email, send_to_email, text)

server.quit()
print('Process is finished!')
