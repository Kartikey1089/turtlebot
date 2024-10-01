import serial
import time

# Establish serial connection (adjust 'port' if needed)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Give time for the connection to establish

# Send command to turn on the motor
ser.write(b'F')
print("Command sent to Arduino")

# Wait a bit to ensure communication
time.sleep(5)

# Close the serial connection
ser.close()
