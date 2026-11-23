times = '1h 45m,360s,25m,30m 120s,2h 60s'

parts=times.split(",")
total_minutes = 0
for time in parts:
    
    parts2=time.split(" ")
    for time1 in parts2:
        
        if "h" in time1:
            hours = int(time1.replace("h", ""))
           
            total_minutes+=hours * 60
        if "m" in time1:
            minutes = int(time1.replace("m", ""))
            
            total_minutes += minutes
        if "s" in time1:
            secundus = int(time1.replace("s", ""))
            
            total_minutes += secundus / 60
print(total_minutes)