#!/usr/bin/env python3

from datetime import date
import os

from input_days import two_dates

T = date.today()

BDAY = [2017, 5, 20] # Y-M-D format .. for easy comparison
TODAY = [T.year, T.month, T.day]

try:
    BDAY, TODAY = two_dates()
    *Today_YM, Today_Day  = TODAY
    *Bday_YM, Bday_Day  = BDAY
except ValueError:
    os.system("clear||cls")
    print("\nInput Error ...Using Simba's Bday as default...")
    BDAY = [2017, 5, 20] # Y-M-D format .. for easy comparison
    TODAY = [T.year, T.month, T.day]
    *Today_YM, Today_Day  = TODAY
    *Bday_YM, Bday_Day  = BDAY
    # to do - import from two_dates later to clean code

def isleap_year(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0: return True
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
    if count_date == Today_YM:
        return counted_days
    # while True: # to run recrusively
    counted_days += month_days(*count_date)
    count_date = new_countday(*count_date)
    return  days_passed(counted_days, count_date)

def main():
    if BDAY == TODAY:
        return 0
    elif BDAY > TODAY:
        print("\nCheck the BDAY\n")
        return None

    count_date = Bday_YM
    days_aged = Today_Day - Bday_Day
    print("\nNo of Days so far: {}\n".format(days_passed(days_aged, count_date)))
    return days_passed(days_aged, count_date)


if __name__ == '__main__':
    main()
