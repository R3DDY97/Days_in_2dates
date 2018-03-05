#!/usr/bin/env python3

from datetime import datetime
import os

def two_dates():
    now = datetime.now()
    today = [now.year, now.month, now.day]
    bday = []
    os.system("clear||cls")
    ymd = input("\nEnter birthdate in YYYY-MM-DD format: ")
    # while True:
    if ymd:
        try:
            bday = [int(i) for i in ymd.split("-")]
            return bday, today
        except ValueError:
            os.system("clear||cls")
            print("wrong date")
    return None

if __name__ == '__main__':
    two_dates()
