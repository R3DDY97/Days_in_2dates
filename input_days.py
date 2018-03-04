#!/usr/bin/env python3

from datetime import datetime
import os

def two_dates():
    now = datetime.now()
    today = [now.year, now.month, now.day]
    bday = []
    os.system("clear||cls")
    YMD = input("\nEnter birthdate in Y-M-D format: ")
    while True:
        try:
            bday = [int(i) for i in YMD.split("-")]
        except ValueError:
            # print("\nInvalid input and to exit press CTRL+C\n or try once again\n\n")
            os.system("clear||cls")
            print("wrong date")
        except KeyboardInterrupt:
            os.sys.exit()
        break
    return bday, today

if __name__ == '__main__':
    two_dates()
