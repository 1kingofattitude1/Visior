import RPi.GPIO as gpio
from SensorsTestRPi_Support import SensorsTest

from settings import SensorSettings
class VisiorIRSense():

    setting_ = ""

    def __init__(self):
        self.setting_ = SensorSettings()
        gpio.setmode(gpio.BCM)
        gpio.setup(self.setting_.FRONT_IR_PIN , gpio.IN)
        gpio.setup(self.setting_.BOTTOM_IR_PIN , gpio.IN)


    def __del__(self):
        gpio.cleanup()




if __name__ == "__main__":
    print("Hello")
    VisiorIRSense()
