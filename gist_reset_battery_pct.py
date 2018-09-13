from dronekit import connect

TARGET_SYSTEM = 0
TARGET_COMPONENT = 0
SEQUENCE_NUMBER = 0
MAV_CMD_RESET_BATTERY_PCT = 301
MAV_CMD_DISABLE_BATT_FAILSAFE = 302

def resetBatteryPercentage(vehicle):
    msg = vehicle.message_factory.command_long_encode(
        TARGET_SYSTEM, TARGET_COMPONENT, MAV_CMD_RESET_BATTERY_PCT,
        0, 0, 0, 0, 0, 0, 0, 0)
    vehicle.send_mavlink(msg)

def disableBatteryFailsafe(vehicle):
    msg = vehicle.message_factory.command_long_encode(
        TARGET_SYSTEM, TARGET_COMPONENT, MAV_CMD_DISABLE_BATT_FAILSAFE,
        0, 0, 0, 0, 0, 0, 0, 0)
    vehicle.send_mavlink(msg)

vehicle = connect('udp:127.0.0.1:14551', wait_ready=False, baud=57600)
vehicle.wait_ready(True, raise_exception=None)
