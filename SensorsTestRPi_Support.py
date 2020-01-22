from time import sleep, time
from settings import Settings, SensorSettings
from platform import system

from time import sleep
from tkinter import *

from MessageBox import messagebox
from settings import Settings

import RPi.GPIO as gpio


class SensorsTest:
    TestWindow = ""
    TestHistory = ""
    TestHistory_Scroll = ""
    ThreadList = []
    checkbox_vals = ""
    multiple_tests = ""
    checkbox_calls_labels = ""
    next_call_allowed = True

    FrontIRPin = ""
    BottomIRPin = ""

    settings_ = ""
    
    HirozontalPan = ""
    VerticalPan = ""
    
    HorizontalPanPin = ""
    VerticalPanPin = ""

    def __init__(self):
        if system().lower() == 'windows':
            messagebox("Error ", "Cannot Execute -> Needed Platform Raspbian ")
            exit()

        else:


            self.settings_ = Settings()
            self.TestWindow = Tk()
            self.TestWindow.overrideredirect(
            self.settings_.isOverRideAlloweded())  # if plf.system().lower() == 'windows' else self.window.wm_attributes("-type","splash")
            self.TestWindow.resizable(0, 0)
            self.TestWindow.config(bg = self.settings_.getBgColor())
            self.TestWindow.geometry(self.settings_.getResolution())
            self.TestWindow.geometry(f"+{abs(4)}+{abs(4)}")
            ###### GPIO SETUP#########
            self.settings_ = SensorSettings()
            
            self.FrontIRPin = self.settings_.FRONT_IR_PIN
            self.BottomIRPin = self.settings_.BOTTOM_IR_PIN

            
            gpio.setmode(gpio.BCM)
            gpio.setup(self.FrontIRPin, gpio.IN)
            gpio.setup(self.BottomIRPin, gpio.IN)
            
            
            self.HorizontalPanPin = self.settings_.HORIZONTAL_LOOK
            self.VerticalPanPin = self.settings_.VERTICAL_LOOK
            
            gpio.setup(self.settings_.VERTICAL_LOOK,gpio.OUT)
            gpio.setup(self.settings_.HORIZONTAL_LOOK,gpio.OUT)
            
            self.VerticalPan = gpio.PWM(self.settings_.VERTICAL_LOOK, 100)
            self.HorizontalPan = gpio.PWM(self.settings_.HORIZONTAL_LOOK, 100)
            

        
        
        
        

    def RedirectCallTo(self, id):
        if id == 0:
            self.InfraredSensorTest(id, "Front")
        elif id == 1:# and self.next_call_allowed:
            self.InfraredSensorTest(id, "Bottom")
        elif id == 2 :#and self.next_call_allowed:
            self.VideoTest(id)
        elif id == 3 :#and self.next_call_allowed:
            self.MotorsTest(id)
        elif id == 4 :#and self.next_call_allowed:
            self.CameraMovementTest(id)

    def TestController(self, checkbox_vals, multiple_tests, checkbox_calls_labels):
        self.checkbox_vals = checkbox_vals.copy()
        self.checkbox_calls_labels = checkbox_calls_labels.copy()
        Header = Label(self.TestWindow, font = ("Courier bold", 12), text = "Testing",
                       width = len("  VISIOR'S On Board Sensor Test"),
                       fg = "#2ade2a",
                       bg = "black")
        Header.pack(side = "top")

        if multiple_tests == True:
            latch = False

            for i in range(len(checkbox_vals)):
                print(checkbox_vals[i].get())
                if checkbox_vals[i].get() == 1:
                    Header.configure(
                        text = "Started " + self.checkbox_calls_labels.get(i)[1].split("\n")[1].replace(")",
                                                                                                        "") + "Test")
                    Header.update()
                    if latch == False:
                        self.TestHistory = Text(self.TestWindow, height = 30, width = 40, fg = "#2ade2a", bg = "black",
                                                borderwidth = 0, highlightthickness = 0)
                        self.TestHistory_Scroll = Scrollbar(orient = "vertical", bg = "red", relief = "flat", width = 9)
                        self.TestHistory.configure(yscrollcommand = self.TestHistory_Scroll.set)
                        self.TestHistory_Scroll.pack(side = "right", fill = "y")
                        self.TestHistory.pack(side = "top", pady = 17, fill = "x")
                        self.TestHistory_Scroll.config(command = self.TestHistory.yview)
                        latch = True
                    self.RedirectCallTo(i)
            Button(self.TestWindow, font = ("Courier bold", 9), text = "\u274c", command = self.TestWindow.destroy,
                   width = 4, bg = "black",
                   fg = "red",
                   borderwidth = 0, highlightthickness = 0, activebackground = "black",
                   activeforeground = "white").place(relx = 0.91, rely = 0.0)
            messagebox("Test Result", "Tests Completed !")


        else:
            for i in range(len(checkbox_vals)):
                print(checkbox_vals[i].get())
                if checkbox_vals[i].get() == 1:
                    Button(self.TestWindow, font = ("Courier bold", 9), text = "\u274c",
                           command = self.TestWindow.destroy, width = 4, bg = "black",
                           fg = "red",
                           borderwidth = 0, highlightthickness = 0, activebackground = "black",
                           activeforeground = "white").place(relx = 0.91, rely = 0.0)
                    Label(self.TestWindow, font = ("Courier bold", 12),
                          text = "Started " + checkbox_calls_labels.get(i)[1].split("\n")[1].replace(")", "") + "Test",
                          width = len("  VISIOR'S On Board Sensor Test"),
                          fg = "#2ade2a",
                          bg = "black").pack(side = "top")
                    self.TestHistory = Text(self.TestWindow, height = 30, width = 40, fg = "#2ade2a", bg = "black",
                                            borderwidth = 0, highlightthickness = 0)
                    self.TestHistory_Scroll = Scrollbar(orient = "vertical", bg = "red", relief = "flat", width = 9)
                    self.TestHistory.configure(yscrollcommand = self.TestHistory_Scroll.set)
                    self.TestHistory_Scroll.pack(side = "right", fill = "y")
                    self.TestHistory.pack(side = "top", pady = 17, fill = "x")
                    self.TestHistory_Scroll.config(command = self.TestHistory.yview)
                    self.RedirectCallTo(i)
                    messagebox("Test Result",
                               checkbox_calls_labels.get(i)[1].split("\n")[1].replace(")", "") + " Tests Completed !")
                    break
        self.TestWindow.mainloop()

    def InfraredSensorTest(self, id, _Sensor):
        PinRead = ""
        if _Sensor.lower() == "front":
            PinRead = self.FrontIRPin
        else:
            PinRead = self.BottomIRPin
        test_init_text = '''Please Keep and Remove Objects in ''' + _Sensor + ''' of IRSensor to complete the test\nStarting IR Test.......\n'''
        start_time = time()
        data_sum = 0
        test_status_flag = False
        self.TestHistory.config(fg = "red")
        self.TestHistory.delete(1.0, END)
        self.TestHistory.update()
        self.TestHistory.insert(END, test_init_text)
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        self.TestHistory.config(fg = "#2ade2a")
        sleep(0.5)
        i = 0
        self.TestHistory.insert(END, ">>> Please Bring Object Near to Sensor \n")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        sleep(5)
        tout = self.settings_.getTestTimeOut()
        while time() - start_time < tout // 2:
            data_sum += gpio.input(PinRead)
            print(data_sum)
            self.TestHistory.insert(END, _Sensor + " IRSensor Test Iteration   %d  - val : %d" % (
            i, data_sum) + "......... Completed  \n")
            self.TestHistory.yview_moveto(1)
            sleep(0.5)
            self.TestWindow.update()
            i += 1

        if data_sum < 5:
            self.next_call_allowed = True
            test_status_flag = True
        else:
            self.next_call_allowed = False
            test_status_flag = False

        self.TestHistory.insert(END, ">>> Now Please Keep Object Far from Sensor \n")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        sleep(5)
        start_time = time()
        while time() - start_time < tout // 2:
            data_sum += gpio.input(PinRead)
            print(data_sum)
            self.TestHistory.insert(END, _Sensor + " IRSensor Test Iteration   %d  - val : %d" % (
            i, data_sum) + "......... Completed  \n")
            self.TestHistory.yview_moveto(1)
            sleep(0.5)
            self.TestWindow.update()
            i += 1
        if data_sum > 0:
            self.next_call_allowed = False
            test_status_flag = True
        else:
            self.next_call_allowed = False
            test_status_flag = False

        if test_status_flag == True:
            self.TestHistory.insert(END, _Sensor + " Ir Sensor Test Completed Succesfully  ")
            self.TestHistory.yview_moveto(1)
            sleep(0.5)
            self.TestWindow.update()
        else:
            self.TestHistory.config(fg = "red")
            self.TestHistory.insert(END, _Sensor + " Ir Sensor Test Failed\nEither Sensor in Disconnected or Damaged  ")
            self.TestHistory.yview_moveto(1)
            sleep(0.5)
            self.TestWindow.update()

    def VideoTest(self, id):
        self.TestHistory.delete("1.0", END)
        self.TestHistory.update()

        for i in range(100):
            self.TestHistory.insert(END, "Video test %d" % (i) + ".........\n")
            self.TestHistory.yview_moveto(1)
            sleep(0.06)
            self.TestWindow.update()

    def MotorsTest(self, id):
        self.TestHistory.delete("1.0", END)
        self.TestHistory.update()

        for i in range(100):
            self.TestHistory.insert(END, "Motors test %d" % (i) + ".........\n")
            self.TestHistory.yview_moveto(1)
            sleep(0.06)
            self.TestWindow.update()

    def CameraMovementTest(self, id):
        self.TestHistory.delete("1.0", END)
        self.TestHistory.update()
        
        test_init_text = '''Do Not Touch or Hold the Module while test is running\nor this might damage the module\nStarting Camera Pan Test.......\n'''
        self.TestHistory.insert(END, test_init_text)
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        
        sleep(10)
        
        
        self.VerticalPan.start(0)
        self.HorizontalPan.start(0)
        
        gpio.output(self.VerticalPanPin,True)
        gpio.output(self.HorizontalPanPin , True)
        
        self.TestHistory.insert(END, "Horizontal Position Reset... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        self.HorizontalPan.ChangeDutyCycle(200/22+2)
        sleep(0.5)
        
        self.TestHistory.insert(END, "Vertical Position Reset... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        self.VerticalPan.ChangeDutyCycle(150/16+2)
        sleep(0.5)
        
        
        self.TestHistory.insert(END, "\nRunning Turning Test ...\n>>>Started Right Pan Test ... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        for duty in range(0,23,1):
            self.TestHistory.insert(END, f"\nTurning Right with Duty Cycle Value {duty}...")
            self.TestHistory.yview_moveto(1)
            self.TestWindow.update()
            self.HorizontalPan.ChangeDutyCycle(duty)
            self.VerticalPan.ChangeDutyCycle(duty)
            sleep(0.5)
                
        print("Switch ...")
        self.TestHistory.insert(END, "\n>>>Started Left Pan Test ... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        for duty in range(23,-1,-1):
            print("- duty cycle")
            self.TestHistory.insert(END, f"\nTurning Left with Duty Cycle Value {duty}...")
            self.TestHistory.yview_moveto(1)
            self.TestWindow.update()
            self.HorizontalPan.ChangeDutyCycle(duty)
            self.VerticalPan.ChangeDutyCycle(duty)
            sleep(0.5)
        
        self.TestHistory.insert(END, "\nHorizontal Position Reset... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        self.HorizontalPan.ChangeDutyCycle(200/22+2)
        sleep(1)
        
        self.TestHistory.insert(END, "\nVertical Position Reset... ")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        self.VerticalPan.ChangeDutyCycle(150/16+2)
        sleep(1)
        
        self.VerticalPan.stop()
        self.HorizontalPan.stop()
        
        
        
        self.TestHistory.insert(END, "\nTest Completed")
        self.TestHistory.yview_moveto(1)
        self.TestWindow.update()
        
        
        messagebox("Test Results","Test Completed !")
        

        #for i in range(100):
         #   self.TestHistory.insert(END, "Camera Movement test %d" % (i) + ".........\n")
          #  self.TestHistory.yview_moveto(1)
           # sleep(0.06)
            #self.TestWindow.update()
