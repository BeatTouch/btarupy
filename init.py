import time
from pyfirmata import Arduino
from playsound import playsound

# Define the port where Arduino is connected
port = '/dev/ttyACM0'

# Establish a connection with the Arduino
board = Arduino(port)
print("Communication Successfully started")

# Set up the pin modes
led_pin = board.digital[9]

#Play a sound function
def punch():
    playsound('sounds/orchestral-cymbals.mp3')
    print('playing punch sound')

# Blink the LED
while True:
    led_pin.write(1)  # Turn the LED on
    board.pass_time(1) # Delay for 1 second
    print("LED ON...")
    #punch()

    led_pin.write(0)  # Turn the LED off
    board.pass_time(1) # Delay for 1 second
    print("LED OFF...")
