seconds= int(input())
minutes = 0
hours = (seconds/ 60) / 60

if(hours != 0):
    hours_rest = seconds - ((int(hours) * 60) * 60)
    minutes = hours_rest / 60
    if(minutes != 0):
        seconds = hours_rest - (int(minutes) * 60)
    else:
        seconds = hours_rest
else:
    minutes = seconds / 60
    if (minutes != 0):
        seconds = seconds - (int(minutes) * 60)
    else:
        seconds = hours / 60 

print(f"{int(hours)}:{int(minutes)}:{int(seconds)}")