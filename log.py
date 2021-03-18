# Code written by - Eng. Mohammed Jassim
# QMR-KWT telemetry data extractor v0.1 2021
# Thie code will fetch the telemtry data from the QMR-KWT and store them in a log (.csv) file.

#### Assumptions ####
# Assuming that we have 
#       - OBC Type1 with ARM Cortex M7 processor using STM32F427
#       - 2x 3-Axis Accelerometers via I2C protocol
#       - 2x 3-Axis Digital Compass via I2C protocol
#       - 6 outputs for Temperature Sensors via SPI
#       - 3 outputs for Gyroscopes via SPI

#  Depends of on the pattern of data that will be provided by the OBC, the data 
# will stored as follows:

# Define required libraries
import random   
import time
import csv
import datetime

######### Define required arrays for storing telemetry data #########

# Acceleration sensor arrays (sensor 1 and 2 and average)
accel_1 = {}
accel_2 = {}
avg_accel = {}

# Compass sensor arrays (sensor 1 and 2 and average)
compass_1 = {}
compass_2 = {}
avg_compass = {}

# Gyroscop sensor array
gyro = {}

# Temeperature sensor variable
temp = 0

# Variable to set the real time clock (RTC) value
rtc = 0;

counter = 0
# Function to compute the sensors data. In the mean time this function will randomlly set values for the sensors
# Once the type communication with the OBC is clear this function will be replaced
# Communication with the OBC might be via serial communication protocol according to a datasheet for OBC Type 1
# found online but we need to verify that becuase each sensor might communicate with the OBC differntly I2C, SPI, ADC, etc.
def randomData():
    # Set random values for the accelerometers (ax, ay, az)
    accel_1[0] = accel_2[0] = random.randrange(-50, 50)
    accel_1[1] = accel_2[1] = random.randrange(-50, 50)
    accel_1[2] = accel_2[2] = random.randrange(-50, 50)

    # Compute the avarage both accelerometers
    avg_accel[0] = (accel_1[0] + accel_2[0])/2
    avg_accel[1] = (accel_1[1] + accel_2[1])/2
    avg_accel[2] = (accel_1[2] + accel_2[2])/2

    # Set random values for the compasses (cx, cy, cz)
    compass_1[0] = compass_2[0] = random.randrange(-50, 50)
    compass_1[1] = compass_2[1] = random.randrange(-50, 50)
    compass_1[2] = compass_2[2] = random.randrange(-50, 50)

    # Compute the avarage both compasses
    avg_compass[0] = (compass_1[0] + compass_2[0])/2
    avg_compass[1] = (compass_1[1] + compass_2[1])/2
    avg_compass[2] = (compass_1[2] + compass_2[2])/2

    # Set random values for the gyroscope parameters (gx, gy, gz)
    # In the front end these parameters will be translated intro pitch, roll and yaw coordinates.
    gyro[0] = random.randrange(-90, 90)
    gyro[1] = random.randrange(-45, 45)
    gyro[2] = random.randrange(0, 10)

    # Set the temperature value betweem -170 C and 123 C assuimg
    # this is the range of space temperature in the LEO.
    temp = random.randrange(-170, 123)
    
    # Check the current date and time stamp and store it in variable
    now = datetime.datetime.now()

    # Format the data and time to "year-month-day hours-minutes-seconds"
    now = now.strftime("%Y-%m-%d %H:%M:%S")     

    data = [{
    'rtc': now,
    'ax': avg_accel[0],
    'ay': avg_accel[1],
    'az':avg_accel[2],
    'cx':avg_compass[0],
    'cy':avg_compass[1],
    'cz':avg_compass[2],
    'gx':gyro[0],
    'gy':gyro[1],
    'gz':gyro[2],
    'temp':temp}]

    fields = ['rtc', 'ax', 'ay', 'az','cx', 'cy', 'cz','gx', 'gy', 'gz','temp'] 

    # Define a CSV to save the telemetry data. This file need to
    # be sent back to the ground station.
    with open('telemetry.csv', 'a', newline='') as csvfile:
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        # writing headers (field names)

        # writing data rows 
        writer.writerows(data)

    return data

def printHeader():
    fields = ['rtc', 'ax', 'ay', 'az','cx', 'cy', 'cz','gx', 'gy', 'gz','temp'] 
    with open('telemetry.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
# * -------------------- RUN SERVER -------------------- *
if __name__ == '__main__':
    printHeader()
    while counter < 30:
        print(randomData())
        time.sleep(1)
        counter = counter + 1


