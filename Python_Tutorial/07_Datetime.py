# Datetime

import datetime

dir(datetime)	# ['date', 'datetime', 'timedelta'...]

# date
gvr = datetime.date(1956, 1, 31)
print(gvr)	# 1956-01-31
print(gvr.year)	# 1956
print(gvr.month)	# 1
print(gvr.day)	# 31

# timedelta
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
print(mill + dt)	# 2000-04-10

# format
print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))
# GVR was born on Tuesday, January 31, 1956.

# date & time & datetime
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

now = datetime.datetime.today()
print(now)	# current datetime to microsecond

# convert strings to datetime
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(
	moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)	# 1969-07-20 00:00:00