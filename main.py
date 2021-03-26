import pandas as pd
from  datetime import datetime, timedelta

from pandas.io.formats.format import return_docstring

file = "projectt.xlsx"
data = pd.read_excel(file, sheet_name=0) 
# index_date = data.columns.get_loc("LastPaidDate")

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
        person = data.iloc[row,:]
        msg = f"{person['Name']} is due for payment with an outstanding balance of {person['Balance']} of {person['TotalFee']}"
        msgs.append(msg)
    return msgs

