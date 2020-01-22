from time import sleep
from tkinter import *

from MessageBox import messagebox
from settings import Settings


class SensorsTest:
    TestWindow = ""
    TestHistory = ""
    TestHistory_Scroll = ""
    ThreadList = []
    checkbox_vals = ""
    multiple_tests = ""
    checkbox_calls_labels = ""
    message_box = ""

    def __init__(self):
        settings_ = Settings()
        self.TestWindow = Tk()
        self.TestWindow.overrideredirect(
            settings_.isOverRideAlloweded())  # if plf.system().lower() == 'windows' else self.window.wm_attributes("-type","splash")
        self.TestWindow.resizable(0, 0)
        self.TestWindow.config(bg = settings_.getBgColor())
        self.TestWindow.geometry(settings_.getResolution())
        self.TestWindow.geometry(f"+{abs(4)}+{abs(4)}")

    def RedirectCallTo(self, id):
        if id == 0:
            self.FrontUltraSonicTest(id)
            print("fsonic called")
        elif id == 1:
            self.BottomUltrasonicTest(id)
            print("bsonic called")
        elif id == 2:
            self.VideoTest(id)
        elif id == 3:
            self.MotorsTest(id)
        elif id == 4:
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

    def FrontUltraSonicTest(self, id):

        self.TestHistory.delete(1.0, END)
        self.TestHistory.update()
        for i in range(100):
            self.TestHistory.insert(END, "Front Ultrasonic test %d" % (i) + ".........\n")
            self.TestHistory.yview_moveto(1)
            sleep(0.06)
            self.TestWindow.update()

    def BottomUltrasonicTest(self, id):

        self.TestHistory.delete(1.0, END)
        self.TestHistory.update()

        for i in range(100):
            self.TestHistory.insert(END, "Bottom Ultrasonic test %d" % (i) + ".........\n")
            self.TestHistory.yview_moveto(1)
            sleep(0.06)
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

        for i in range(100):
            self.TestHistory.insert(END, "Camera Movement test %d" % (i) + ".........\n")
            self.TestHistory.yview_moveto(1)
            sleep(0.06)
            self.TestWindow.update()
