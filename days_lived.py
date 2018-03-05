#!/usr/bin/env python3

from datetime import date
import os
from input_days import two_dates

try:
    BDAY, TODAY = two_dates()
except (ValueError, TypeError):
    print("\nInput Error ...Using Simba's Bday as default...")
    T = date.today()
    BDAY, TODAY = [2017, 5, 20], [T.year, T.month, T.day]  #Y-M-D -for easy date list comparison

*TODAY_YM, TODAY_DAY = TODAY
*BDAY_YM, BDAY_DAY = BDAY


def isleap_year(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return True
    elif year%100 == 0 and year%400 == 0:
        return True
    return False

def month_days(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if isleap_year(year):
            return 29
        return 28
    return 31

def new_countday(year, month):
    if month < 12:
        return [year, month+1]
    return [year+1, 1]

def days_passed(counted_days, count_date):
    if count_date == TODAY_YM:
        return counted_days
    counted_days += month_days(*count_date)
    count_date = new_countday(*count_date)
    return  days_passed(counted_days, count_date)

def main():
    if BDAY == TODAY:
        return 0
    elif BDAY > TODAY:
        print("\nCheck the BDAY\n")
        return None

    count_date = BDAY_YM
    days_aged = TODAY_DAY - BDAY_DAY
    print("\nNo of Days so far: {}\n".format(days_passed(days_aged, count_date)))
    return days_passed(days_aged, count_date)


if __name__ == '__main__':
    os.system("clear||cls")
    main()
