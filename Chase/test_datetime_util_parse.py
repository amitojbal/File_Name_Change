from datetime import datetime as dt
import dateutil.parser


f_string = '20200611'

print(f_string)

f_change = dateutil.parser.parse(f_string)

print(f_change)
print("f_current_dt", f_change)
print("f_date", f_change.date())
print("f_year", f_change.year)
print("f_month", f_change.month)
print("f_day", f_change.day)
print("f_time", f_change.time())
print("f_hour", f_change.hour)
print("f_minute", f_change.minute)
print("f_sec", f_change.second)
print("f_mic secs", f_change.microsecond)



# f_date = dt.strptime(f_change, '%Y%-b-%d %H:%M:%S')

# print(f_date)
# f_date, f_name = f_change.split(' ')

# print(f_date)