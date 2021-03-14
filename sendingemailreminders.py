# Import libraries
import pandas as pd 
import smtplib 

# My credentials and name 
your_name = 'Chioma Uche'
your_email = 'codepersontest@gmail.com'
your_password = 'Chiomabobo123'

# Set up the email server to send the email 
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# Read the file 
email_list = pd.read_excel("projectt.xlsx")

# Get all the names, email addresses, subjects and messages 
all_names = email_list['Name']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']
all_last_paid_date = email_list['Last Paid Date'] 
all_future_pay_date = email_list['Future Pay Date'] 
all_total_fee_to_be_paid = email_list['Total Fee To Be Paid'] 
all_amount_paid = email_list['Amount Paid']
all_balance_due = email_list['Balance Due']
all_paid = email_list['Paid']

# Loop through the emails 
for idx in range(len(all_emails)):
    # Get each records name, email, subject and message 
    name = all_names[idx]
    email = all_emails[idx]
    subject = all_subjects[idx]
    messsage = all_messages[idx]
    lastpaiddate = all_last_paid_date[idx]
    futurepaydate = all_future_pay_date[idx] 
    totalfeestobepaid = all_total_fee_to_be_paid[idx] 
    lastamountpaid = all_amount_paid[idx]
    balancedue = all_balance_due[idx] 
    paid = all_paid[idx]
    # Create the email to send
    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(your_name, your_email, name, email, subject, message, lastpaiddate, futurepaydate, totalfeestobepaid, lastamountpaid, balancedue, paid ) )
    # In the email field, you can add multiple other emails if you want 
    # All of them to receive the same text 
    try: 
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e: 
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
# Close the smtp server 
server.close()     
