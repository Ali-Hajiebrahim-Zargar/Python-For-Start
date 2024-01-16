from datetime import datetime, date, time, timezone

print("Please enter the data:")
a = input()
b = a.split("/")
b = list(map(int,b))
if int(b[1]) > 12 or int(b[2]>31):
    print("WRONG")
   
else:    
    dt = datetime.strptime(a, "%Y/%m/%d").date()
    dt_now = datetime.strptime(datetime.now().strftime("%Y/%m/%d"), "%Y/%m/%d").date()
    print(dt_now)
    diff = dt_now - dt
    print(diff.days//365)