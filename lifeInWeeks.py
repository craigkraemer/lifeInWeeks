# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:36:34 2022

@author: craig
"""

from datetime import date

today = date.today().strftime('%m-%d-%Y')
birthdate = input("What is your birthdate in MM/DD/YYYY format? ")

today_0 = today[0]
today_1 = today[1]
today_months = today_0 + today_1
today_months = int(today_months)

today_3 = today[3]
today_4 = today[4]
today_days = today_3 + today_4
today_days = int(today_days)

today_6 = today[6]
today_7 = today[7]
today_8 = today[8]
today_9 = today[9]
today_years = today_6 + today_7 + today_8 + today_9
today_years = int(today_years)

month_0 = birthdate[0]
month_1 = birthdate[1]
birth_month = month_0 + month_1
birth_month = int(birth_month)

day_3 = birthdate[3]
day_4 = birthdate[4]
birth_day = day_3 + day_4
birth_day = int(birth_day)

year_6 = birthdate[6]
year_7 = birthdate[7]
year_8 = birthdate[8]
year_9 = birthdate[9]
birth_year = year_6 + year_7 + year_8 + year_9
birth_year = int(birth_year)

months_in_days = (today_months - birth_month) * 30.4368499167
days = (today_days - birth_day)
years_in_days = (today_years - birth_year) * 365.242199

total_days = months_in_days + days + years_in_days
days_left = (90 * 365.242199) - total_days
weeks_left = days_left / 7
weeks_left = int(weeks_left)
print(weeks_left)

