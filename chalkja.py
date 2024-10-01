import serial
import time

# Open the serial connection to the Arduino
# Replace '/dev/ttyACM0' with the correct port (check with ls /dev/tty* if unsure)
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Give some time for the connection to establish

def send_command(command):
    arduino.write(command.encode())  # Send command to Arduino
    time.sleep(0.5)  # Small delay

try:
    while True:
        # Example: Toggle between turning the LED on and off
        command = input("Enter 1 to turn ON LED, 0 to turn OFF LED: ")
        if command in ['1', '0']:
            send_command(command)
        else:
            print("Invalid input. Enter '1' or '0'.")
            
except KeyboardInterrupt:
    print("Program stopped")

finally:
    arduino.close()  # Close the serial connection
