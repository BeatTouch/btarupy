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
led_pin = board.digital[9]
piezo_plate_input = board.get_pin('a:3:i') 

piezo_plate_input.mode = INPUT
piezo_plate_input.enable_reporting()

#Play a sound function
def punch():
    playsound('sounds/orchestral-cymbals.mp3')
    print('playing punch sound')

# Blink the LED
while True:
    print(piezo_plate_input.read())
    time.sleep(0.1)
    if(piezo_plate_input.read() > 0.0):
        led_pin.write(1)
        time.sleep(0.4)
        led_pin.write(0)

