import datetime
from time import strftime

def saving():
    print('=============================\n' +
        'Starting saving plan program\n' +
        '=============================')
    amount = input('Please enter the amount you want to save: ')
    amount_parsed = ''
    for char in amount:
        if char.isdigit():
            amount_parsed += char
    date_entry = input('Please enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date.today()
    date2 = datetime.date(year, month, day)
    delta = (date2 - date1).days
    daily_saving = int(amount_parsed) / delta
    print(f'To reach the goal you need to save ${daily_saving} per day')