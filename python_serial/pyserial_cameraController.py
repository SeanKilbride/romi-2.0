# Importing Libraries
import serial
import time
import csv

# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data

def read_serial():
    time.sleep(0.05)
    # x = arduino.read()          # read one byte
    # s = arduino.read(10)        # read up to ten bytes (timeout)
    line = arduino.readline()   # read a '\n' terminated line    
    return line

def print_instructions():
    print("\nWelcome to the OV7675 test\n")
    print("Available commands:\n")
    print("single (s) - take a single image and print out the hexadecimal for each pixel (default)")
    print("live (l) - the raw bytes of images will be streamed live over the serial port")
    print("capture (c) - when in single mode, initiates an image capture\n")

def take_send_input(arduino):
    # take input
    usr_ip = input("\nEnter one of the above available commands: ") # take input command from user
    if usr_ip == 's':
        usr_ip = 'single'
    elif usr_ip == 'l':
        usr_ip = 'live'
    elif usr_ip == 'c':
        usr_ip = 'capture'
    elif usr_ip not in ['single', 'live', 'capture']:
        print('command not acccepted')
        return

    # send input
    print('sending command <{}> to ARDUINO' .format(usr_ip)) # printing the value
    arduino.write(bytes(usr_ip, 'utf-8'))
    response = read_serial()
    print(response)
    return

def read_save_serial(arduino):
    # read serial
    try:
        ser_bytes = arduino.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        # print(decoded_bytes)

        # save serial
        with open("serialTest/test_data.csv","a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([time.time(),decoded_bytes])
    except:
        # print("Keyboard Interrupt")
        return

### _______ SETUP ___________ ###
print('running setup...\n')
time.sleep(1)

# print instructions:
print_instructions()

# take user input and send to arduino
take_send_input(arduino)


### _______ MAIN LOOP _______ ###
print('running main loop...\n')
while True:
    # take_send_input(arduino)
    read_save_serial(arduino)
