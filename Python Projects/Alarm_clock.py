from datetime import datetime
from playsound import playsound
alarm_setting_time=input("Enter alarm time in the format HH:MM:SS ") #06:02:00:PM
hours=alarm_setting_time[0:2]
minutes=alarm_setting_time[3:5]
seconds=alarm_setting_time[6:8]
am_pm=alarm_setting_time[9:].upper()
print(hours,minutes,seconds,am_pm)
print(datetime.now())
while True:
    now = datetime.now()
    cur_hour = now.strftime("%H")
    cur_min = now.strftime("%M")
    cur_sec = now.strftime("%S")
    cur_am_pm = now.strftime("%p")
    if am_pm==cur_am_pm and hours==cur_hour and minutes==cur_min and seconds==cur_sec:
        print("Wake Up!")
        playsound('beautiful_spring_melody.mp3')
        break

