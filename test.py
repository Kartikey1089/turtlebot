import serial
import time

# Replace '/dev/ttyUSB0' with your Arduino port (it may be /dev/ttyACM0 or similar)
arduino_port = '/dev/ttyUSB0'  
baud_rate = 9600

# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for Arduino to initialize

# Blink LED on Arduino
print("Sending '1' to turn on the LED")
ser.write(b'1')  # Send '1' to turn the LED on
time.sleep(2)

print("Sending '0' to turn off the LED")
ser.write(b'0')  # Send '0' to turn the LED off
time.sleep(2)

# Close the serial connection
ser.close()
