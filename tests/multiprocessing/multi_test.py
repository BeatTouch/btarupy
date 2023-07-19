import multiprocessing
import time
from playsound import playsound

#Play a sound function
def ride1():
    playsound('sounds/ride_1.ogg')
    print('playing r1de 1 sound')

def ride2():
    playsound('sounds/ride_2.ogg')
    print('playing ride 2 sound')


def add():
    ride1()

def sud():
    ride2()

if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=add)
    p = multiprocessing.Process(name='p', target=sud)
    p1.start()
    p.start()
