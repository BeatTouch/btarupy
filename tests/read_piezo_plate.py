import time
import multiprocessing
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
    playsound('sounds/tom_m.ogg')
    print('playing ride 2 sound')


piezo_plate_1_input.read()
piezo_plate_2_input.read()
time.sleep(0.1)

def plate1Input():
    if(piezo_plate_1_input.read() > 0.2):
        print("Plate 1: " + str(piezo_plate_1_input.read()))
        led_pin1.write(1)
        
        playsound('sounds/tom_m.ogg')
        time.sleep(0.1)
        led_pin1.write(0)


def plate2Input():
    if(piezo_plate_2_input.read() > 0.2):
        print("Plate 2: " + str(piezo_plate_2_input.read()))
        led_pin2.write(1)
        
        playsound('sounds/rim.ogg')
        time.sleep(0.1)
        led_pin2.write(0)


if __name__ == '__main__':
    while True:
        p1 = multiprocessing.Process(name='p1', target=plate1Input)
        p = multiprocessing.Process(name='p', target=plate2Input)

        p1.start()
        p.start()

        time.sleep(0.1)
