import datetime as dt
import time

print('Welcome to your birthday countdown')

year = int(input('Which year were you born in?\n'))
month = int(input('Which month (1 for Jan, 2 for Feb, and so on)?\n'))
day = int(input('Which day in that month?\n'))

date_birth = dt.datetime(year, month, day)

weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_num = date_birth.weekday()
print('You may have forgotten which day of the week it was ...')
print('But I can tell you ... it was a ...', end = ' ')
print(weekday_names[weekday_num])


current_time = dt.datetime.now()
thisyear = current_time.year
thisyear_bday = dt.datetime(thisyear, month, day)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    next_bday = dt.datetime(thisyear+1, month, day)
    
print('Your next birthday will be on ...', end = ' ')
print(next_bday)
print()
print('That will be a ...', end = ' ')
weekday_num = next_bday.weekday()
print(weekday_names[weekday_num])

print()
print()

dd = next_bday - current_time

days_left = dd.days
total_seconds_left = dd.seconds

# print(type(dd))

# We will convert seconds to HRS, MIN, SEC
seconds_left = total_seconds_left % 60
total_mins_left = total_seconds_left//60
hrs_left = total_mins_left//60
minutes_left = total_mins_left % 60


total_mins_left, seconds_left  = divmod(total_seconds_left, 60)
hrs_left, minutes_left  = divmod(total_mins_left, 60)




#print('Your next birthday is', days_left, 'days', hrs_left, 'hrs', minutes_left, 'mins', seconds_left, 'secs away.')
input()



while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time
    days_left = dd.days
    total_seconds_left = dd.seconds

    # We will convert seconds to HRS, MIN, SEC
    seconds_left = total_seconds_left % 60
    total_mins_left = total_seconds_left//60
    hrs_left = total_mins_left//60
    minutes_left = total_mins_left % 60

    print('Your next birthday is', days_left, 'days', hrs_left, 'hrs', minutes_left, 'mins', seconds_left, 'secs away.', end = '\r')

    time.sleep(1)












