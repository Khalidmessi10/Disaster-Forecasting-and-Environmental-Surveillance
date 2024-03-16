import os
import serial
import csv
import time
from datetime import datetime

# Open the serial port
ser = serial.Serial('COM10', 9600)  # Adjust the port and baudrate accordingly

filename = 'sensor_data.csv'

# Check if the file is empty
file_empty = os.stat(filename).st_size == 0

# Create a CSV file and write headers if the file is empty
with open(filename, mode='a', newline='') as file:
    writer = csv.writer(file)
    if file_empty:
        writer.writerow(['Datetime', 'Humidity', 'Temperature', 'Rain Level', 'X', 'Y', 'Z', 'CO2 Level', 'Dust Density'])

# Read data from serial port and store in CSV file
while True:
    line = ser.readline().decode('utf-8').strip()
    print("Received:", line)  # Debugging statement to check received data
    if line.startswith('Humidity'):
        humidity = line.split('=')[1].strip()
    elif line.startswith('Temperature'):
        temperature = line.split('=')[1].strip()
    elif line.startswith('Rain Level'):
        rain_level = line.split(':')[1].strip().split('%')[0]
    elif line.startswith('X'):
        x_value = line.split(':')[1].strip()  # Extract X value
    elif line.startswith('Y'):
        y_value = line.split(':')[1].strip()  # Extract Y value
    elif line.startswith('Z'):
        z_value = line.split(':')[1].strip()  # Extract Z value
        # Get current datetime
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Append data to CSV file
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Check if CO2 Level and Dust Density are defined
            if 'co2_level' not in locals():
                co2_level = ''
            if 'dust_density' not in locals():
                dust_density = ''
            writer.writerow([current_datetime, humidity, temperature, rain_level, x_value, y_value, z_value, co2_level, dust_density])
            print("Data written")
    elif line.startswith('CO2 Level'):
        co2_level = line.split(':')[1].strip().split(' ')[0]
    elif line.startswith('Dust Density'):
        dust_density = line.split(':')[1].strip().split(' ')[0]
    time.sleep(1)  # Adjust the sleep duration if necessary
