#!/usr/bin/env python3

from datetime import *

class Payout():
    def __init__(self, hour, minute):
        self.payTime = time(hour, minute)
    users = []

myPayout = Payout(17, 30)
#print ("Payout time: " + myPayout.payTime.isoformat())

print ("Payout time: " + str(myPayout.payTime))

currentTime = datetime.now()

delta_hours = myPayout.payTime.hour - currentTime.hour
delta_minutes = myPayout.payTime.minute - currentTime.minute + 60

print ("Time until payout: " + str(delta_hours) + ":" + str(delta_minutes))
