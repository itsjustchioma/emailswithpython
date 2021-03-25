# sending emails and files.

import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
# to add attachments,
from email.mime.base import MIMEBase 
from email import encoders 
import os.path

email = 'codepersontest@gmail.com' #your email
password = 'Chiomabobo123'
send_to_email = 'chiomauchenwosu@gmail.com' #sender's email
subject = 'This is the subject' #sybject/header
message = 'This is my message.' #body of email
# location of the file you want to send
file_location = r"C:\Users\user\Documents\attachfile.txt" 
#converts normal string to raw string

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain')) #attach the message using a mimetext object while declaring it as plain text

filename = os.path.basename(file_location)#parsing file location
attachment = open(file_location, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= vendor")

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587) #creating a connection to Google's smtp server
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
print('Email sent!')
