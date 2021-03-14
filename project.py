# this predicts the future dates i.e, a month later 

import pandas as pd #pip install openpyxl
from datetime import datetime 
from datetime import timedelta # timedelta helps with future dates 


file = "projectt.xlsx"
df = pd.read_excel(file)

# to find the date in thirty days and send the payment notice, 
exceldate0 = df.iloc[0, 4]
futuredate0 = str(datetime.now() + timedelta(days=30))
print('In 30 days time, it will be', (exceldate0) + timedelta(days=30))

exceldate1 = df.iloc[1, 4]
futuredate1 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate1) + timedelta(days=30))

exceldate2 = df.iloc[2, 4]
futuredate2 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate2) + timedelta(days=30))

exceldate3 = df.iloc[3, 4]
futuredate3 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate3) + timedelta(days=30))

exceldate4 = df.iloc[4, 4]
futuredate4 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate4) + timedelta(days=30))

exceldate5 = df.iloc[5,4]
futuredate5 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate5) + timedelta(days=30))

exceldate6 = df.iloc[6, 4]
futuredate6 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate6) + timedelta(days=30)) 

exceldate7 = df.iloc[7, 4]
futuredate7 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate7) + timedelta(days=30))

exceldate8 = df.iloc[8, 4]
futuredate8 = str(datetime.now() + timedelta(days=30))
#if exceldate < futuredate:
print('In 30 days time, it will be', (exceldate8) + timedelta(days=30))


