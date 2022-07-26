from datetime import datetime
import calendar


def years():
    currYear = datetime.now().year
    ourYears = [str(i) for i in range(currYear - 150, currYear - 14, 1)]
    ourYears.insert(0, "year")
    return ourYears


def months():
    ourMonths = list(calendar.month_name)
    ourMonths[0] = "month"
    return ourMonths


def days(year, month, flag: int):
    ourDays = ["day"]
    if flag > 0:
        ourDays.extend([str(i) for i in range(1, calendar.monthrange(int(year), int(month))[1] + 1)])
    # print(ourDays)
    return ourDays
