from dronekit import connect, APIException
import serial
import time

lost_connection = False

def heartbeatCallback(self, attr_name, value):
    global lost_connection
    lost_connection = value > 5
        
def printInitialVehicleAttributes(vehicle):
    print 'Get some vehicle attribute values:'
    print 'GPS: %s' % (vehicle.gps_0)
    print 'Battery: %s' % (vehicle.battery)
    print 'Last Heartbeat: %s' % (vehicle.last_heartbeat)
    print 'Is Armable?: %s' % (vehicle.is_armable)
    print 'System status: %s' % (vehicle.system_status.state \
                                 if vehicle.system_status else None)
    print 'Mode: %s' % (vehicle.mode.name if vehicle.mode else None)

vehicle = connect('COM16', baud=57600, wait_ready=False)
vehicle.add_attribute_listener('last_heartbeat', heartbeatCallback)
#vehicle.wait_ready(True, raise_exception=False)
printInitialVehicleAttributes(vehicle)

while True:
    if lost_connection:
        try:
            vehicle = connect('COM16', baud=57600, wait_ready=False)
            vehicle.add_attribute_listener('last_heartbeat', heartbeatCallback)
        except serial.SerialException:
            pass
        except APIException as e:
            print e
    else:
        print vehicle.mode.name
        time.sleep(3)
