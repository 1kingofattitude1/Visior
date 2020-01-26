import os
from time import sleep

import pigpio

from settings import SensorSettings


class AngluarSweep():
    NECK_PIN = 17
    HEAD_PIN = 27
    CURRENT_VERTICAL_ANGLE = 500
    CURRENT_HORIZONTAL_ANGLE = 500
    AngularPi = ""

    def setPigpio(self):
        try:
            Ss = SensorSettings()
            self.NECK_PIN = Ss.HORIZONTAL_LOOK
            self.HEAD_PIN = Ss.VERTICAL_LOOK
            os.system("sudo pigpiod")
            print("pigpio deamon is up ...")
        except Exception as e:
            pass

    def __init__(self):
        self.setPigpio()
        self.AngularPi = pigpio.pi()
        print("Angular Pi Init")
        self.AutoReset()


def AutoReset(self):
    self.AngularPi.set_servo_pulsewidth(self.NECK_PIN, 1250)
    self.AngularPi.set_servo_pulsewidth(self.HEAD_PIN, 1250)
    sleep(0.9)
    print("reset ")


def VerticalAngleChange(self, angle = 0):
    if 500 <= self.CURRENT_VERTICAL_ANGLE <= 2300:
        print("Vertical Pan")
        self.AngularPi.set_servo_pulsewidth(self.HEAD_PIN, 500 + angle * 9)
        sleep(0.1)
        self.CURRENT_VERTICAL_ANGLE += (500 + angle + 20)
        if self.CURRENT_VERTICAL_ANGLE < 500:
            self.CURRENT_VERTICAL_ANGLE = 500
        elif self.CURRENT_VERTICAL_ANGLE > 2300:
            self.CURRENT_VERTICAL_ANGLE = 2300
    else:
        self.CURRENT_VERTICAL_ANGLE = 1250
        self.AutoReset()


def HorizontalAngleChange(self, horizontal_angle = 0):
    if 500 <= self.CURRENT_VERTICAL_ANGLE <= 2300:
        self.AngularPi.set_servo_pulsewidth(self.NECK_PIN, 500 + horizontal_angle * 8)
        sleep(0.1)
        self.CURRENT_HORIZONTAL_ANGLE += (500 + horizontal_angle + 20)
        if self.CURRENT_HORIZONTAL_ANGLE < 500:
            self.CURRENT_HORIZONTAL_ANGLE = 500
        elif self.CURRENT_HORIZONTAL_ANGLE > 2300:
            self.CURRENT_HORIZONTAL_ANGLE = 2300
    else:
        self.CURRENT_HORIZONTAL_ANGLE = 1250
        self.AutoReset()


def FreeSweep(self, direction = "vertical"):
    for i in range(700, 1600, 1):
        if direction == "vertical":
            self.AngularPi.set_servo_pulsewidth(self.HEAD_PIN, i)
            sleep(0.005)
        else:
            self.AngularPi.set_servo_pulsewidth(self.NECK_PIN, i)
            sleep(0.005)
    for i in range(1600, 701, -1):
        if direction == "vertical":
            self.AngularPi.set_servo_pulsewidth(self.HEAD_PIN, i)
            sleep(0.005)
        else:
            self.AngularPi.set_servo_pulsewidth(self.NECK_PIN, i)
            sleep(0.005)
    self.AutoReset()


class CameraPanDriver(AngluarSweep):
    pi = ""
    SWEEP_VAL = 500
    VERTICAL_LOOK_ANGLE = 500
    ROT_SPEED = 20

    def __init__(self):
        super().__init__()
        self.pi = pigpio.pi()
        print("Rc Pi init")
        self.SWEEP_VAL = 500
        self.VERTICAL_LOOK_ANGLE = 500

    def ResetToNormal(self):
        self.SWEEP_VAL = 1250
        self.VERTICAL_LOOK_ANGLE = 1250
        self.pi.set_servo_pulsewidth(self.NECK_PIN, 1250)
        self.pi.set_servo_pulsewidth(self.HEAD_PIN, 1250)
        sleep(0.9)
        print("reset ")

    def PanLeft(self):
        if self.SWEEP_VAL <= 2300:
            print("Looking Left")
            self.pi.set_servo_pulsewidth(self.NECK_PIN, self.SWEEP_VAL)
            self.SWEEP_VAL += self.ROT_SPEED
        else:
            self.ResetToNormal()

    def PanRight(self):
        if self.SWEEP_VAL >= 500:
            print("Looking Right")
            self.pi.set_servo_pulsewidth(self.NECK_PIN, self.SWEEP_VAL)
            self.SWEEP_VAL -= self.ROT_SPEED
        else:
            self.ResetToNormal()

    def PanUp(self):
        if self.VERTICAL_LOOK_ANGLE >= 500:
            print("Looking Up")
            self.pi.set_servo_pulsewidth(self.HEAD_PIN, self.VERTICAL_LOOK_ANGLE)
            self.VERTICAL_LOOK_ANGLE -= self.ROT_SPEED
        else:
            self.ResetToNormal()

    def PanDown(self):
        if self.VERTICAL_LOOK_ANGLE <= 2000:
            print("Looking Down")
            self.pi.set_servo_pulsewidth(self.HEAD_PIN, self.VERTICAL_LOOK_ANGLE)
            self.VERTICAL_LOOK_ANGLE += self.ROT_SPEED
        else:
            self.ResetToNormal()
