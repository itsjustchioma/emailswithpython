import datetime 
import calendar 
import smtplib 
from email.mime.text import MIMEText 

now = datetime.datetime.now()

today_date = datetime.date.today()

cy = now.year 
cm = now.month 

last_day = calendar.monthrange(cy,cm)[1] 
