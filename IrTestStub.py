from time import time
from random import randrange
from platform import platform,system

if system().lower() == 'windows':
    pass
else:
    import RPi.GPIO as gpio

def IrTestStub():

    if randrange(1,500)%2 == 0:
        return True
    return False

def GroundConnect():
    return IrTestStub()




