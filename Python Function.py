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

tid = timedelta(00,00,00)
thour = 00
tidArray = []

for i in range (121):
    tid = tid + timedelta(minutes=5)
    tidmin = tid/60
    if tidmin == 60:
        thour = thour + 1
    print(tidmin) 
    tidArray.append(tidmin) 
    
print (tidArray)
