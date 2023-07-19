import time
from pyfirmata import Arduino, INPUT, util
from playsound import playsound

# Define the port where Arduino is connected
port = '/dev/ttyACM0'

# Establish a connection with the Arduino
board = Arduino(port)
print("Communication Successfully started")
it = util.Iterator(board)  
it.start()  

# Set up the pin modes
led_pin1 = board.digital[8]
led_pin2 = board.digital[11]

piezo_plate_1_input = board.get_pin('a:1:i') 
piezo_plate_2_input = board.get_pin('a:4:i') 

piezo_plate_1_input.mode = INPUT
piezo_plate_2_input.mode = INPUT

piezo_plate_1_input.enable_reporting()
piezo_plate_2_input.enable_reporting()

#Play a sound function
def ride1():
    playsound('sounds/ride_1.ogg')
    print('playing r1de 1 sound')

def ride2():
    playsound('sounds/ride_2.ogg')
    print('playing ride 2 sound')


piezo_plate_1_input.read()
piezo_plate_2_input.read()
time.sleep(0.1)

# Blink the LED 
while True:
    if(piezo_plate_1_input.read() > 0.0):
        print("Plate 1: " + str(piezo_plate_2_input.read()))
        led_pin1.write(1)
        ride1()
        time.sleep(0.1)
        led_pin1.write(0)

    if(piezo_plate_2_input.read() > 0.0):
        print("Plate 2: " + str(piezo_plate_2_input.read()))
        led_pin2.write(1)
        ride2()
        time.sleep(0.1)
        led_pin2.write(0)

