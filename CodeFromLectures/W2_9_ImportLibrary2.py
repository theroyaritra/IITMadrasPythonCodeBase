print('We shall import the calendar library and other libraries in 5 different ways and note the differences in code :-')
import calendar #First way to import
print(calendar.month(2000,4)) # Shows the calendar of the 4th month in the year 2000 AD.
print(calendar.calendar(2021)) #Displays the entire calendar of the year 2021 AD.
'''
from calendar import * # Second way to import [Not an optimum way as we are importing everything from the calendar library]

print(calendar(2020)) # Prints entire calendar of the year 2020 AD. Note here we do not use calendar.calendar() since we already imported everything(meant by *)  from the calendar library.

print(month(2024,8)) # Shows the calendar  of the 8th months in the year 2024 AD. Note here we do not use calendar.calendar() since we already imported everything(meant by *)  from the calendar library.

'''
from calendar import month # 3rd Way to import
print(month(2020,4))

import random as c # 4th way to import
print(c.randrange(1,10))

from math import sqrt as b #5th way to import
print(b(64))