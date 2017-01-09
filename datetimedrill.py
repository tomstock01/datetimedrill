# Python version 2.7.12
# Author: Tom Stock
# Python Drill datetime
# Based on the current time in Portland find out if the New York City
# and London branches are open or closed.

import datetime

now = datetime.datetime.today()

NYtime = now + datetime.timedelta(hours=3)
Londontime = now + datetime.timedelta(hours=8)


if (NYtime.hour >=9 and NYtime.hour <21):
    print "The New York City Branch is open!"
else:
    print "The New York City Branch is closed."


if (Londontime.hour >=9 and Londontime.hour <21):
    print "The London branch is open!"
else:
    print "The London branch is closed."
