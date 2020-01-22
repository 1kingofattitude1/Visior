import RPi.GPIO as gpio
from time import sleep


class CameraMotion:
    UpDownPin = 2
    LeftRightPin = 3

    PwmUpDown = ""
    PwmLeftRight = ""

    Frequency = 100

    UpDownCurPos = 0
    LeftRightCurPos = 0

    def __init__(self):
        try:

            gpio.setmode(gpio.BCM)
            gpio.setup(self.UpDownPin, gpio.OUT)
            gpio.setup(self.LeftRightPin, gpio.OUT)
            self.PwmUpDown = gpio.PWM(self.UpDownPin, self.Frequency)
            self.PwmLeftRight = gpio.PWM(self.LeftRightPin, self.Frequency)
            self.PwmUpDown.start(0)
            self.PwmLeftRight.start(0)
            gpio.output(self.UpDownPin, True)
            gpio.output(self.LeftRightPin, True)

        except Exception as e:
            print(f"Exception in <Class> - CameraMoition  <Function> -  __init__  <File> - CameraMotion  -> {e}")
            pass

    def __del__(self):
        try:
            self.PwmLeftRight.stop()
            self.PwmUpDown.stop()
            gpio.cleanup()
        except Exception as e:
            print(f"Exception in __del__ in CameraMoition {e}")
            pass

    def ResetCameraPosition(self, caller=None):
        try:
            self.LeftRightCurPos = 200 // 22 + 2
            self.UpDownCurPos = 110 // 16 + 2
            if caller == "usonic":
                print(f"Vertical reset .. caller  = {caller}")
                self.PwmUpDown.ChangeDutyCycle(110 / 16 + 2)
                sleep(0.04)
            else:
                print(f"Horizontal reset .. caller  = {caller}")
                self.PwmLeftRight.ChangeDutyCycle(200 / 22 + 2)
                sleep(0.03)
                print(f"Vertical reset .. caller  = {caller}")
                self.PwmUpDown.ChangeDutyCycle(150 / 16 + 2)
                sleep(0.03)
            print("Camera Module Reset ..")


        except Exception as e:
            print(
                f"Exception in <Class> - CameraMoition  <Function> -  ResetCameraPosition  <File> - CameraMotion  -> {e}")
            pass

    def RunDutyCycle(self, PwmModule, start, end, step, sleep_time):
        for itr in range(start, end, step):
            PwmModule.ChangeDutyCycle(itr)
            sleep(sleep_time)

    def CameraMotionTest(self):
        try:
            print("\n############## Testing Started  #############")
            print("Starting Left Right Pan Test .. ")
            self.RunDutyCycle(self.PwmLeftRight, 0, 24, 1, 0.05)
            self.RunDutyCycle(self.PwmLeftRight, 24, -1, -1, 0.05)
            print("Left Right Pan Test Complete !!")

            print("Starting Up Down Pan Test .. ")
            self.RunDutyCycle(self.PwmUpDown, 0, 24, 1, 0.05)
            self.RunDutyCycle(self.PwmUpDown, 24, -1, -1, 0.05)
            print("Up Down Pan Test Complete !!")
            print("\n############## Testing Ended  #############\n")

            self.ResetCameraPosition()

        except Exception as e:
            print(
                f"Exception in <Class> - CameraMoition  <Function> -  CameraMotionTest  <File> - CameraMotion  -> {e}")
            pass

    def RemoteController(self, rec_key):
        try:

            delays = 0.03
            if rec_key == "'r'":
                print("Reset Key Pressed")
                self.ResetCameraPosition()
            ##############  Left Right Moition  ##############
            if rec_key == "'a'":
                print("check a")
                if self.LeftRightCurPos < 24:
                    self.RunDutyCycle(self.PwmLeftRight, self.LeftRightCurPos, self.LeftRightCurPos + 2, 1, delays)
                    self.LeftRightCurPos += 2
                    if self.LeftRightCurPos > 23:
                        self.LeftRightCurPos = 23
                    print("Turning Left")
                else:
                    # self.RunDutyCycle(self.PwmLeftRight , 23 , 21,-1,delays)
                    self.LeftRightCurPos = 23
            # self.ResetCameraPosition()

            elif rec_key == "'d'":
                print("check d")
                if self.LeftRightCurPos > 0:
                    self.RunDutyCycle(self.PwmLeftRight, self.LeftRightCurPos, self.LeftRightCurPos - 2, -1, delays)
                    self.LeftRightCurPos -= 2
                    if self.LeftRightCurPos < 0:
                        self.LeftRightCurPos = 0
                    print("Turning Right")
                else:
                    # self.RunDutyCycle(self.PwmLeftRight , 0 , 2,1,delays)
                    self.UpDownCurPos = 0
            # self.ResetCameraPosition()

            ##############  Up Down Moition  ##############
            elif rec_key == "'w'":
                print("check w")
                if self.UpDownCurPos < 24:
                    self.RunDutyCycle(self.PwmUpDown, self.UpDownCurPos, self.UpDownCurPos + 2, 1, delays)
                    self.UpDownCurPos += 2
                    if self.UpDownCurPos > 23:
                        self.UpDownCurPos = 23
                    print("Turning Left")
                else:
                    self.UpDownCurPos = 23
            # self.ResetCameraPosition()

            elif rec_key == "'s'":
                print("check s")
                if self.UpDownCurPos > 0:
                    self.RunDutyCycle(self.PwmUpDown, self.UpDownCurPos, self.UpDownCurPos - 2, -1, delays)
                    self.UpDownCurPos -= 2
                    if self.UpDownCurPos < 0:
                        self.UpDownCurPos = 0
                    print("Turning Right")
                else:
                    self.UpDownCurPos = 0
            # self.ResetCameraPosition()
        except Exception as e:
            print(
                f"Exception in <Class> - CameraMoition  <Function> -  RemoteController  <File> - CameraMotion  -> {e}")
            pass

