import serial
import time
import keyboard

# Establish serial connection with Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Give time for the connection to establish

print("Use arrow keys to control the bot. Press 'q' to quit.")

try:
    while True:
        if keyboard.is_pressed('up'):
            ser.write(b'F')  # Forward
            print("Moving Forward")
            time.sleep(0.5)
        
        elif keyboard.is_pressed('down'):
            ser.write(b'B')  # Backward
            print("Moving Backward")
            time.sleep(0.5)
        
        elif keyboard.is_pressed('left'):
            ser.write(b'L')  # Turn left
            print("Turning Left")
            time.sleep(0.5)
        
        elif keyboard.is_pressed('right'):
            ser.write(b'R')  # Turn right
            print("Turning Right")
            time.sleep(0.5)
        
        elif keyboard.is_pressed('q'):
            print("Exiting...")
            break
        
        # Read and print encoder values
        if ser.in_waiting > 0:
            encoder_value = ser.readline().decode('utf-8').rstrip()
            print("Encoder Value:", encoder_value)
        
except KeyboardInterrupt:
    print("Program interrupted")

finally:
    ser.close()
