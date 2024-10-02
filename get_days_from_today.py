from datetime import datetime

def get_days_from_today(date):
    try:
        #Converting a string into a datetime object
        date = datetime.strptime(date, '%Y-%m-%d')
        #get current date
        date_today = datetime.today()
        #get difference between current date and given date
        diff = date_today - date

        return diff.days
    except ValueError:
        return "Value Error"

print(get_days_from_today("2021-10-09"))