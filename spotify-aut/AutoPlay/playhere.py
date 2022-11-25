from datetime import timedelta, datetime

# https://www.guru99.com/date-time-and-datetime-classes-in-python.html#:~:text=What%20is%20Timedelta%20in%20Python,some%20delta%20date%20and%20time.

sec  = 60
# s = get_current_time()
now = datetime.now()
print("now   ",now)

print("future",now + timedelta(seconds=sec))