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

piezo_plate_1_input = board.get_pin('a:1:i')
piezo_plate_2_input = board.get_pin('a:2:i')
piezo_plate_3_input = board.get_pin('a:3:i')
piezo_plate_4_input = board.get_pin('a:4:i') 

piezo_plate_1_input.mode = INPUT
piezo_plate_2_input.mode = INPUT
piezo_plate_3_input.mode = INPUT
piezo_plate_4_input.mode = INPUT

piezo_plate_1_input.enable_reporting()
piezo_plate_2_input.enable_reporting()
piezo_plate_3_input.enable_reporting()
piezo_plate_4_input.enable_reporting()

piezo_plate_1_input.read()
piezo_plate_2_input.read()
piezo_plate_3_input.read()
piezo_plate_4_input.read()

time.sleep(0.1)

def plate1Input():
    if(piezo_plate_1_input.read() > 0.2):
        print("Plate 1: " + str(piezo_plate_1_input.read()))        
        playsound('sounds/crash_3.ogg')

def plate2Input():
    if(piezo_plate_2_input.read() > 0.2):
        print("Plate 2: " + str(piezo_plate_2_input.read()))        
        playsound('sounds/hihat_closed.ogg')

def plate3Input():
    if(piezo_plate_3_input.read() > 0.2):
        print("Plate 3: " + str(piezo_plate_3_input.read()))
        playsound('sounds/kick.ogg')

def plate4Input():
    if(piezo_plate_4_input.read() > 0.2):
        print("Plate 4: " + str(piezo_plate_4_input.read()))       
        playsound('sounds/tom_sh.ogg')

if __name__ == '__main__':
    while True:
        p1 = multiprocessing.Process(name='p1', target=plate1Input)
        p2 = multiprocessing.Process(name='p2', target=plate2Input)
        p3 = multiprocessing.Process(name='p3', target=plate3Input)
        p4 = multiprocessing.Process(name='p4', target=plate4Input)

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        time.sleep(0.1)
