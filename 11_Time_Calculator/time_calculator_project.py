def add_time (start, duration):
    start_hour = int(start[:1]) if len(start) == 7 else int(start[:2])
    start_minute = int(start[2:4]) if len(start) == 7 else int(start[3:5])
    duration_hour = int(duration[:1]) if len(duration) == 4 else int(duration[:2])
    duration_minute = int(duration[2:]) if len(duration) == 4 else int(duration[3:])
    current_time = start[-2:]
    
    
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
    if new_minute > 59:
        new_hour += 1
        new_minute = new_minute - 60
        
    if new_hour > 12 and current_time == 'AM':
        new_hour = new_hour - 12
        current_time = 'PM'
    elif new_hour > 12 and current_time == 'PM':
        new_hour = new_hour - 12
        current_time == 'AM'
    
    new_time = f'{new_hour}:{new_minute} {current_time}'
    
    return new_time

print(add_time("3:30 PM", "2:12"))