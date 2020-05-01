import datetime
import pytz
'''
	Coordinated Universal Time (UTC) is the primary time standard
	 by which the world regulates clocks and time.
	
	Greenwich Mean Time (GMT) is a time zone and UTC is a time standard.

	A timezone's offset refers to how many hours the timezone is from Coordinated Universal Time (UTC).

	NAIVE VS AWARE TIMEZONE:
	
	Naive datetime:
		Naive datetime does not have information about timezone and daylight saving.
		Naive time is easier to work with.

	Awared datetime:
		Awared datetime have information about timezone and daylight saving.

	The easiest way to tell if a datetime object is naive or awared is by checking tzinfo.
	tzinfo will be set to None if the object is naive.

	A naive datetime object is limited in that it cannot locate itself
	in relation to offset aware datetime objects.
	 	
'''

#-----------------------#
#     DATE AND TIME     #
#-----------------------#
date_time = datetime.datetime(2020, 1, 9)
print("Date and time: ", date_time)

#-----------------------#
#         DATE          #
#-----------------------#
date = datetime.date(2020, 1, 9)
print("Date: ",date)

#-----------------------#
#         TIME          #
#-----------------------#
time = datetime.time()
print("Time: ", time)

#-----------------------#
#      Current Date     #
#-----------------------#
today = datetime.date.today()
print("Current Date: ", today)
print("Year:", today.year, "\nMonth:", today.month, "\nDay:", today.day)

#-----------------------#
#       WEEK DAY        #
#-----------------------#
# Monday 0
# Sunday 6
print(today.weekday()) 
# Monday 1 
# Sunday 7
print(today.isoweekday())

#-----------------------#
#       TIME DELTA      #
#-----------------------#
# To perform operations on date and time
print(today)
# timedelta
tdelta = datetime.timedelta(days=7)
# date1
print(f'Today Date: {today}')
# date2
print(f'Expected Date: {today + tdelta}')

# date2 = date1 +/- timedelta
# timedelta = date1 +/- date2

bday = datetime.date(2021, 1, 1)
till_bday = bday - today
print("Days left for birthday: ", till_bday.days)
print("Seconds left for birthday: ", till_bday.total_seconds())

#-----------------------#
#         TIME          #
#-----------------------#

time = datetime.time(6, 45, 30, 100000)
print("Time: ", time)
print("Hour:", time.hour, "\nMinutes:", time.minute, "\nSeconds:", time.second)


#---------------------------#
#       DATE AND TIME       #
#---------------------------#
dt = datetime.datetime.now()
# dt = datetime.datetime(2020, 6, 4, 16, 32, 44, 100)
print("Date and Time:", dt)
print("Date:         ", dt.date())
print("Time:         ", dt.time())

tdelta = datetime.timedelta(hours=4)
print(dt + tdelta)

# Current datetime
dt_today  = datetime.datetime.today()
dt_now    = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print("datetime.today: ", dt_today)   # local time with timezone (none)
print("datetime.now:   ", dt_now)     # can pass timezone, if leave empty then (today & now) are similar
print("datetime.utcnow:", dt_utcnow)  # not timezone awared datetime, tzinfo is set to none

# To get timezone awared datetime, we need to explicitly set those by using pytz.
dt = datetime.datetime(2018, 9, 6, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print("now    ",dt_now)
# does not have option to pass timezone as param
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("utc_now",dt_utcnow)

## .now() is preferred to use for awared date time.

## To get my timezone awared datetime
dt_now = datetime.datetime.now(tz=pytz.UTC)
my_dt = dt_now.astimezone(pytz.timezone('Asia/Karachi'))
print(my_dt)

## Make naive datetime timezone awared
naive_dt = datetime.datetime.now()
tz = pytz.timezone('Asia/Karachi')
naive_dt = tz.localize(naive_dt)
print(naive_dt)

print("---------------------")

my_date = datetime.datetime.now(tz = pytz.timezone('Asia/Karachi'))

## Convert datetime to string:
#  IsoFormat
print(my_date.isoformat()) # international standard datetime
#  Using your own format:
print(my_date.strftime("%B %d, %Y"))

## Convert string into datetime:
dt_str = 'January 13, 2020'
print(datetime.datetime.strptime(dt_str, '%B %d, %Y'))


## arrow popular package for datetime



print("---------------------")

# Display all timezones
timezones = pytz.all_timezones
# for index, zone in enumerate(timezones):
# 	print(index, "----", zone)

# Check timezone is naive?
naive = datetime.datetime.now()
print(naive.tzinfo)

# Check timezone is aware?
d = datetime.datetime.now()
timezone = pytz.timezone("America/Los_Angeles")
d_aware = timezone.localize(d)
print(d_aware.tzinfo)

## TypeError: can't compare offset-naive and offset-aware datetimes

# d_naive = datetime.datetime.now()
# timezone = pytz.timezone("America/Los_Angeles")
# d_aware = timezone.localize(d_naive)
# d_naive < d_aware