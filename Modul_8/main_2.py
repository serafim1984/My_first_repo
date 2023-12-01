from datetime import date
from datetime import datetime


def get_days_in_month(month, year):

    d1 = datetime(year, month, day = 1)

    d2 = datetime(year if month < 12 else year + 1, month + 1 if month < 12 else 0, day = 1)

    days = d2 - d1

    return days.days
    
    