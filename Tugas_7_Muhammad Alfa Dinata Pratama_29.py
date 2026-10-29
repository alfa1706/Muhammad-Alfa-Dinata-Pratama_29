
#1. Python DateTime
from datetime import datetime

a = datetime(2022, 12, 28, 23, 55, 59, 342380)

print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())

#2. Strftime python
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	

#3. Strptime python
from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

#4. Current date and time python
from datetime import datetime
now = datetime.now()
 
print("now =", now)

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#5. Current time python
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#6. Python timestamp to datetime
from datetime import datetime
 
timestamp = 1545730073

dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

#7. Python time modul
import time

seconds = time.time()

print("Seconds since epoch =", seconds)	

#8. Pyhton sleeptime
import time

time.sleep(2)
print("Wait until 2 seconds.")