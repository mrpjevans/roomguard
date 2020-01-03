import time
import os.path
import automationhat
import apprise

alarm_sounding = False

script_dir = os.path.dirname(os.path.abspath(__file__))

apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add(script_dir + '/.apprise')
apobj.add(config)

print("Arming in 10 seconds")
time.sleep(10)
print("Armed!")

while True:

    # Check the current state of the PIR sensor    
    motion_detected = automationhat.input.three.read()

    # If new motion detected sound the alarm
    if motion_detected and alarm_sounding != True:
        print("Motion detected, loud noise time")
        #automationhat.relay.one.on()
        alarm_sounding = True

        apobj.notify(
            body='Motion detected! Yikes!',
            title='RoomGuard',
        )

    # If motion no longer detected stop the alarm
    if motion_detected != True and alarm_sounding:
        print("It's all gone quiet, switching off")
        automationhat.relay.one.off()
        alarm_sounding = False

        apobj.notify(
            body='No more motion detected',
            title='RoomGuard',
        )

    time.sleep(0.5)
