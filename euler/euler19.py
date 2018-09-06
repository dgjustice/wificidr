"""    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
from itertools import cycle

def is_leap(year):
    """Is year a leap year?"""
    if not (year % 100):
        if not (year % 400):
            return True
        return False
    if not (year % 4):
        return True
    return False

def feb_days(year):
    """How many days in Feb"""
    return 28 if not is_leap(year) else 29


monthdays = [
    ("January", 31),
    ("February", 0),
    ("March", 31),
    ("April", 30),
    ("May", 31),
    ("June", 30),
    ("July", 31),
    ("August", 31),
    ("September", 30),
    ("October", 31),
    ("November", 30),
    ("December", 31)
]

if __name__ == "__main__":
    sun_months = []
    day_cycle = cycle([
        "Sun",
        "Mon",
        "Tues",
        "Wednes",
        "Thurs",
        "Fri",
        "Sat"
    ])
    month_cycle = cycle(monthdays)
    # Start day on 1, Monday
    next(day_cycle)
    for year in range(1900, 2001):
        for month_day in monthdays:
            month = month_day[0]
            days_in_month = month_day[1] or feb_days(year)
            for i in range(days_in_month):
                day = next(day_cycle)
                # print(month, day, i + 1, year)
                if not i and day == "Sun" and year > 1900:
                    print(month, i + 1, year)
                    sun_months.append(1)
    print(len(sun_months))
