#!/usr/bin/env python3

from datetime import *

class Payout():
    def __init__(self, hour, minute):
        self.payTime = datetime(MINYEAR,1,1,hour,minute,0,0)
    users = []

myPayout = Payout(18, 00)

print ("Payout time: " + str(myPayout.payTime))

currentDay = datetime.now()
currentTime = time(currentDay.hour, currentDay.minute)

diff = myPayout.payTime - currentDay
hours = divmod(diff.seconds, 3600)
minutes = divmod(hours[1], 60)

print (str(hours[0]) + ":" + str(minutes[0]))
