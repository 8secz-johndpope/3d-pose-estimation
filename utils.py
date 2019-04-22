def get_time_string(seconds):
    hours = 0
    minutes = 0
    while seconds >= 3600:
        hours += 1
        seconds -= 3600
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)