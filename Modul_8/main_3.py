from datetime import datetime


def get_str_date(date):

    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f%z').strftime('%A %d %B %Y')