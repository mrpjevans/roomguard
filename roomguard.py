import time
import automationhat

alarm_sounding = False

print("Arming in 10 seconds")
time.sleep(10)
print("Armed!")

while True:

    # Check the current state of the PIR sensor    
    motion_detected = automationhat.input.three.read()

    # If new motion detected sound the alarm
    if motion_detected and alarm_sounding != True:
        print("Motion detected, loud noise time")
        automationhat.relay.one.on()
        alarm_sounding = True

    # If motion no longer detected stop the alarm
    if motion_detected != True and alarm_sounding:
        print("It's all gone quiet, switching off")
        automationhat.relay.one.off()
        alarm_sounding = False

    time.sleep(0.5)
