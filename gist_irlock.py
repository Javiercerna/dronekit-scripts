from dronekit import connect
import time

vehicle = connect('udp:127.0.0.1:14551', baud=57600, wait_ready=False)

@vehicle.on_message('LANDING_TARGET')
def handleIRLOCKMeasurements(self, name, msg):
    print msg

while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        vehicle.close()
        break
