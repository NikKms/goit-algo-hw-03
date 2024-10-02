from datetime import datetime

def get_days_from_today(date: str) -> int | str:
    try:
        # 'date' is a string format ("YYYY-MM-DD")
        # Converting the string into a datetime object
        date = datetime.strptime(date, '%Y-%m-%d')
        # Get the current date
        date_today = datetime.today()
        # Calculate the difference between the current date and the given date
        diff = date_today - date

        # Return the difference in days as an integer
        return diff.days
    except ValueError:
        # Return a string with an error message if the format is invalid
        return "Value Error"

print(get_days_from_today("2021-10-09"))

