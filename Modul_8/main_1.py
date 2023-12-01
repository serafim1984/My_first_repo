from datetime import datetime


def get_days_from_today(date):

    delta_days = datetime.now().date() - datetime.fromisoformat(date).date()

    return delta_days.days