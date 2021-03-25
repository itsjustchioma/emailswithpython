# creates a secure connection with Gmail's SMTP server, using the SMTP_SSL() of smtplib to initiate a TLS-encrypted connection.

#SSL = Secure Sockets Layer, TLS = Transport Layer Security

import smtplib #smtplib is used for sending emails to any internet machine with an SMTP or ESMTP listener daemon

sender_address = ("coderpersontest@gmail.com") #my gmail acct

receiver_address = ("coderpersontest@gmail.com")  # any valid email address

account_password = ("Chiomabobo123")

subject = ("Test Email using Python.") #email header/ subject

body = ("Hello from Chioma! \n\n\Happy to hear from you!\nWith regards,\n\Chioma.")

#Endpoint for the SMPT Gmail server (Don't change this!)
smpt_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

print('Email sent!')


