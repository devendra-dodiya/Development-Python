##Function to get bus schedule time
##Function to get time left for bus to arrive
##Function to get time for whole Journey

import random
import os

from datetime import datetime
from datetime import time
from datetime import timedelta

# print(datetime.datetime.now())
# print(datetime.timedelta(minutes=5))
# print(date.time)

# tid = timedelta(00,00,00)
# thour = 00
# tidArray = []

# for i in range (121):
#     tid = tid + timedelta(minutes=5)
#     tidmin = tid/60
#     if tidmin == 60:
#         thour = thour + 1
#     print(tidmin) 
#     tidArray.append(tidmin) 
    
# print (tidArray)


import datetime

def busTidSchedule( Interval ):
    x = datetime.datetime.now()
    for intv in range (280):
        y = x + datetime.timedelta(minutes=5)
        x = y
        busTiming = str(y.time()).split(".")[0]
        Interval.append(busTiming)
    return

def currTime():
    timeN = datetime.datetime.now()
    shortTime = str(timeN.time()).split(".")[0]
    return shortTime

def checkNextBus( kstring, klist ):
    ctime = kstring
    timeIntlist = klist
    if ctime in timeIntlist:
        print("Bus is available ::", ctime)


timeNow=currTime()
timeInterval = []
busTidSchedule(timeInterval)
print(timeInterval)
print("Time now is  :: ", timeNow)
checkNextBus(timeNow,timeInterval)


l1 = ['AA', 'B', 'C', 'D', 'A', 'A', 'C']

# string in the list
if 'A' in l1:
    print('A is present in the list')

# string not in the list
if 'X' not in l1:
    print('X is not present in the list')
