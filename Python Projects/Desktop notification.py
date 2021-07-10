import time
from plyer import notification
import psutil
# function returning time in hh:mm:ss
def convertTime(seconds):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return "%d:%02d:%02d" % (hrs, mins, secs)
battery = psutil.sensors_battery()
print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)
# converting seconds to hh:mm:ss
print("Battery left : ", convertTime(battery.secsleft))
if __name__ == "__main__":
    while True:
        # returns a tuple
        battery = psutil.sensors_battery()
        if battery.percent<80:
            notification.notify(
                title = "ALERT!!!",
                message = "Plug-in charger! Battery left for {}".format(convertTime(battery.secsleft)),
                timeout = 10,
                app_icon="battery_icon.ico"
            )
            time.sleep(3600)