def add_time(start, duration, day=None):
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))
    
    total_minutes = start_hour * 60 + start_minute
    total_minutes += duration_hour * 60 + duration_minute
    
    days_passed = total_minutes // (24 * 60)
    new_minutes = total_minutes % (24 * 60)
    
    new_hour = new_minutes // 60
    new_minute = new_minutes % 60
    
    new_period = period
    if new_hour >= 12:
        new_period = "PM" if period == "AM" else "AM"
    
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12
    
    new_time = f"{new_hour}:{new_minute:02} {new_period}"
    
    if day:
        day = day.lower()
        day_index = (days_of_week.index(day) + days_passed) % 7
        new_day = days_of_week[day_index].capitalize()
        new_time += f", {new_day}"
    
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time
