from dronekit import connect
from pymavlink import mavutil

import time

TARGET_SYSTEM = 0
TARGET_COMPONENT = 0
SEQUENCE_NUMBER = 0

rtcm_1005 = [211, 0, 19, 62, 208, 0, 3, 3, 63, 43, 132, 250, 177, 215, 233, 191, 15, 60, 234, 19, 98, 152, 187, 62, 157]
rtcm_1005_length = len(rtcm_1005)
rtcm_1005 += [0] * (180 - rtcm_1005_length)

rtcm_1077 = [211, 0, 95, 67, 80, 0, 98, 23, 37, 34, 0, 0, 0, 5, 0, 138, 0, 0, 0, 0, 32, 0, 0, 0, 125, 25, 57, 65, 49, 76, 0, 0, 61, 164, 191, 154, 247, 67, 176, 65, 2, 19, 1, 187, 210, 143, 173, 245, 36, 168, 241, 253, 117, 142, 23, 218, 171, 73, 71, 159, 213, 187, 152, 60, 157, 131, 218, 121, 91, 245, 161, 48, 35, 200, 69, 217, 118, 93, 151, 101, 217, 6, 1, 104, 76, 22, 132, 64, 36, 248, 178, 26, 76, 95, 60, 255, 145, 64, 132, 147, 205]
rtcm_1077_length = len(rtcm_1077)
rtcm_1077 += [0] * (180 - rtcm_1077_length)

#rtcm_1087 = [211, 0, 80, 67, 240, 0, 146, 51, 186, 160, 0, 0, 64, 56, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 122, 18, 122, 50, 68, 3, 181, 165, 200, 252, 89, 24, 41, 190, 237, 252, 199, 253, 134, 68, 76, 227, 69, 31, 64, 46, 22, 32, 207, 138, 119, 127, 132, 13, 23, 197, 231, 216, 75, 109, 171, 102, 217, 54, 109, 152, 88, 21, 133, 225, 72, 18, 99, 179, 103, 216, 198, 213, 240, 98, 154, 3]
rtcm_1087 = [211, 0, 80, 67, 240, 0, 146, 67, 121, 224, 0, 0, 64, 56, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 122, 18, 130, 58, 68, 3, 178, 240, 149, 161, 121, 104, 37, 126, 245, 252, 199, 253, 30, 243, 229, 0, 11, 160, 163, 188, 155, 19, 191, 180, 115, 55, 246, 149, 232, 31, 149, 32, 96, 222, 179, 178, 236, 59, 46, 200, 88, 21, 5, 193, 64, 20, 100, 240, 197, 252, 211, 119, 120, 146, 0, 11]
rtcm_1087_length = len(rtcm_1087)
rtcm_1087 += [0] * (180 - rtcm_1087_length)

def sendDGPS(vehicle):
    #msg = vehicle.message_factory.gps_input_encode(0,1,0,0,0,5,-120725880,-770828270,82,0.5,0,0,0,0,0.1,0.1,0.1,14)
    #msg = vehicle.message_factory.gps_input_encode(0,1,252,0,0,5,1343435,103679016,82,1,0,0,0,0,0,0,0,14)
    #for _ in range(500):
        #time.sleep(0.1)
##    seq_num = 0
##    for _ in range(50):
##        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num << 3, rtcm_1005_length, rtcm_1005)
##        vehicle.send_mavlink(msg)
##        seq_num += 1
##        if seq_num > 31:
##            seq_num = 0
##        time.sleep(0.5)
##        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num << 3, rtcm_1077_length, rtcm_1077)
##        vehicle.send_mavlink(msg)
##        seq_num += 1
##        if seq_num > 31:
##            seq_num = 0
##        time.sleep(0.5)
##        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num << 3, rtcm_1087_length, rtcm_1087)
##        vehicle.send_mavlink(msg)
##        seq_num += 1
##        if seq_num > 31:
##            seq_num = 0

    seq_num_1 = 0
    seq_num_2 = 0
    seq_num_3 = 0
    for _ in range(50):
        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num_1 << 3, rtcm_1005_length, rtcm_1005)
        vehicle.send_mavlink(msg)
        seq_num_1 += 1
        if seq_num_1 > 31:
            seq_num_1 = 0
        time.sleep(0.5)
        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num_2 << 3, rtcm_1077_length, rtcm_1077)
        vehicle.send_mavlink(msg)
        seq_num_2 += 1
        if seq_num_2 > 31:
            seq_num_2 = 0
        time.sleep(0.5)
        msg = vehicle.message_factory.gps_rtcm_data_encode(seq_num_3 << 3, rtcm_1087_length, rtcm_1087)
        vehicle.send_mavlink(msg)
        seq_num_3 += 1
        if seq_num_3 > 31:
            seq_num_3 = 0
    
vehicle = connect('udp:127.0.0.1:14551', wait_ready=False, baud=57600)
vehicle.wait_ready(True, raise_exception=None)    
