# Patched .cfg connection for cam frame dims

import os
from tkinter import Button, Label, Tk

import cv2
from PIL import Image, ImageTk
from pynput import keyboard as py_key

from IrTestStub import GroundConnect, IrTestStub
from settings import CameraSettings, Settings


# from CameraMotion import CameraMotion

class RcModeController:
    window = ""
    vid = ""
    width = 0
    height = 0
    canvas = ""
    delay = 15
    photo = ""
    snapshot = ""
    image_count = 0
    CamUp = ""
    CamDown = ""
    CamLeft = ""
    CamRight = ""
    MoveForward = ""
    MoveBackward = ""
    TurnLeft = ""
    TurnRight = ""
    CamMotion = ""
    ground_connect = ""

    AreaClearStr = "\u2714 " + "Front Area Clear"
    ObstacleStr = "\u26A0 " + "Object Detected In Front Of Me"

    GroundContactTrue = "\u2714 " + " Ground Contact True"
    GroundContactNegative = "\u26A0 " + "Ground Contact Negative"

    def __init__(self):
        try:
            settings_ = Settings()
            self.window = Tk()
            self.window.overrideredirect(
                settings_.isOverRideAlloweded())  # if plf.system().lower() == 'windows' else self.window.wm_attributes("-type","splash")
            self.window.geometry(settings_.getResolution())
            self.window.resizable(0, 0)
            self.window.config(bg = settings_.getBgColor())
            w_height, w_width = 640, 490

            width = self.window.winfo_screenwidth()
            height = self.window.winfo_screenheight()
            print(f"width x height -> {width}x{height}")
            self.window.geometry(f"+{abs(0)}+{abs(0)}")
            self.width = 620  # self.window.winfo_screenwidth()
            self.height = 620  # self.window.winfo_screenheight()
            print(f"width x height -> {360}x{360}")
            self.window.focus()

            # self.CamMotion = CameraMotion()
            # self.CamMotion.ResetCameraPosition()
            self.notification = Label(self.window, font = ("Courier bold", 12),
                                      text = "\u26A0 " + "Loading ...", width = 30,
                                      fg = "white",
                                      bg = "black")
            self.notification.place(relx = 0.5, rely = 0.57)

            self.ground_connect = Label(self.window, font = ("Courier bold", 12),
                                        text = "\u26A0 " + "Loading ...", width = 30,
                                        fg = "white",
                                        bg = "black")
            self.ground_connect.place(relx = 0.5, rely = 0.63)

            self.IrSimulator()

        except Exception as e:
            print(f"Exception in <Function> __init__ - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def IrSimulator(self):

        if IrTestStub():
            self.notification.config(fg = "red", text = self.ObstacleStr)
            self.notification.update()
        else:
            self.notification.config(fg = "#2ade2a", text = self.AreaClearStr)
            self.notification.update()

        if GroundConnect():
            self.ground_connect.config(fg = "#2ade2a", text = self.GroundContactTrue)
            self.ground_connect.update()
        else:
            self.ground_connect.config(fg = "red", text = self.GroundContactNegative)
            self.ground_connect.update()

        print("Updated Object Status....")
        self.window.after(1000, self.IrSimulator)

    def ReadPresentImages(self):
        imglist = os.listdir("./Snapshots/")[-1]
        first_split = imglist.split("_")
        second_split = first_split[1].split(".")
        self.image_count = int(second_split[0])
        print(f"image_counter -> {self.image_count}")

    def on_press(self, key):
        b_g = "black"
        f_g = "red"
        # border_w = 3

        if str(format(key)) == "'w'":
            self.CamUp.config(bg = b_g, fg = f_g, font = ("Courier bold", 17))
        if str(format(key)) == "'s'":
            self.CamDown.config(bg = b_g, fg = f_g, font = ("Courier bold", 17))
        if str(format(key)) == "'a'":
            self.CamLeft.config(bg = b_g, fg = f_g, font = ("Courier bold", 17))
        if str(format(key)) == "'d'":
            self.CamRight.config(bg = b_g, fg = f_g, font = ("Courier bold", 17))
        if str(format(key)) == "Key.up":
            self.MoveForward.config(font = ("Courier bold", 16), fg = "red")
        if str(format(key)) == "Key.down":
            self.MoveBackward.config(font = ("Courier bold", 16), fg = "red")
        if str(format(key)) == "Key.left":
            self.TurnLeft.config(font = ("Courier bold", 16), fg = "red")
        if str(format(key)) == "Key.right":
            self.TurnRight.config(font = ("Courier bold", 16), fg = "red")

        print(f"pressed -> {str(format(key))}")

    def on_release(self, key):
        b_g = "black"
        f_g = "#2ade2a"
        # border_w = 1
        if str(format(key)) == "'w'":
            self.CamUp.config(bg = b_g, fg = f_g, font = ("Courier bold", 15))
        if str(format(key)) == "'s'":
            self.CamDown.config(bg = b_g, fg = f_g, font = ("Courier bold", 15))
        if str(format(key)) == "'a'":
            self.CamLeft.config(bg = b_g, fg = f_g, font = ("Courier bold", 15))
        if str(format(key)) == "'d'":
            self.CamRight.config(bg = b_g, fg = f_g, font = ("Courier bold", 15))
        if str(format(key)) == "Key.up":
            self.MoveForward.config(font = ("Courier bold", 14), fg = "#2ade2a")
        if str(format(key)) == "Key.down":
            self.MoveBackward.config(font = ("Courier bold", 14), fg = "#2ade2a")
        if str(format(key)) == "Key.left":
            self.TurnLeft.config(font = ("Courier bold", 14), fg = "#2ade2a")
        if str(format(key)) == "Key.right":
            self.TurnRight.config(font = ("Courier bold", 14), fg = "#2ade2a")

    def StreamScreen(self):
        try:
            self.vid = ""  # cv2.VideoCapture(0)
            print("Opencv init ..")

            listerner = py_key.Listener(
                on_press = self.on_press,
                on_release = self.on_release
            )
            listerner.start()
            print("Key Listener started .. ")

            Label(self.window, font = ("Courier bold", 20), text = "VISIOR'S On Board Camera Stream", width = "1080",
                  fg = "#2ade2a",
                  bg = "black").pack(side = "top")
            Button(self.window, font = ("Courier bold", 10), text = "\u274c", command = self.window.destroy, width = 4,
                   bg = "black",
                   fg = "red",
                   borderwidth = 0, highlightthickness = 0, activebackground = "black",
                   activeforeground = "white").place(relx = 0.91, rely = 0.0)
            Button(self.window, font = ("Courier bold", 11), text = "\u25A3 " + "Snapshot", command = self.SaveFrame,
                   width = 10,
                   bg = "#00e6b8",
                   fg = "black",
                   borderwidth = 3, highlightthickness = 0, activebackground = "black",
                   activeforeground = "white", relief = "ridge").place(relx = 0.005, rely = 0.57)
            Button(self.window, font = ("Courier bold", 11), text = "\u25CF " + "Record", command = self.SaveFrame,
                   width = 10,
                   bg = "black",
                   fg = "#00e6b8",
                   borderwidth = 3, highlightthickness = 0, activebackground = "black",
                   activeforeground = "white", relief = "ridge").place(relx = 0.013 * 2 + 0.15, rely = 0.57)

            self.CreateCameraButtons()
            self.CreateMovementButton()

            self.canvas = Label(self.window, width = CameraSettings().getCamFrameDim("width"),
                                height = CameraSettings().getCamFrameDim("height"), bg = "red")
            self.canvas.pack()

            self.window.mainloop()

        except Exception as e:
            print(f"Exception in <Function> StreamScreen - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass


    def SaveFrame(self):
        try:
            self.image_count += 1
            SSpath = "./SnapShots/snapshot_" + str(self.image_count) + ".jpg"
            cv2.imwrite(SSpath, cv2.cvtColor(self.snapshot, cv2.COLOR_BGR2RGB))
            SavedLoc = Label(self.window, font = ("Courier bold underline", 12),
                             text = f"Snapshot Saved in -> {SSpath}",
                             width = "1080",
                             fg = "white", bg = "black")
            SavedLoc.pack(side = "bottom")
            self.window.after(1000, SavedLoc.forget)
        except Exception as e:
            print(f"Exception in <Function> SaveFrame - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def get_Frame(self):
        try:
            if self.vid.isOpened():
                ret, frame = self.vid.read()
                return ret, cv2.cvtColor(cv2.resize(frame, None, fx = 0.9, fy = 1.4), cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"Exception in <Function> get_Frame - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def update(self):
        try:
            ret, frame = self.get_Frame()
            self.snapshot = frame
            if ret:
                self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.canvas.configure(image = self.photo)
                self.canvas.image = self.photo
            self.window.after(2, self.update)
        except Exception as e:
            print(f"Exception in <Function> update - <Class> RcModeController - <File> TkinterCam.py --> {e}")
            pass

    def CreateCameraButtons(self):

        self.CamUp = Button(self.window, font = ("Courier bold", 15), text = "Ⓦ", width = 4,
                            fg = "#2ade2a",
                            bg = "black",
                            borderwidth = 0, highlightthickness = 0, activebackground = "black",
                            activeforeground = "white")
        self.CamUp.place(relx = 0.25, rely = 0.72)
        self.CamRight = Button(self.window, font = ("Courier bold", 15), text = "Ⓓ", width = 4,
                               fg = "#2ade2a",
                               bg = "black",
                               borderwidth = 0, highlightthickness = 0, activebackground = "black",
                               activeforeground = "white")
        self.CamRight.place(relx = 0.343, rely = 0.79)
        self.CamDown = Button(self.window, font = ("Courier bold", 15), text = "Ⓢ", width = 4,
                              fg = "#2ade2a",
                              bg = "black",
                              borderwidth = 0, highlightthickness = 0, activebackground = "black",
                              activeforeground = "white")
        self.CamDown.place(relx = 0.25, rely = 0.82)
        self.CamLeft = Button(self.window, font = ("Courier bold", 15), text = "Ⓐ", width = 4,
                              fg = "#2ade2a",
                              bg = "black",
                              borderwidth = 0, highlightthickness = 0, activebackground = "black",
                              activeforeground = "white")
        self.CamLeft.place(relx = 0.16, rely = 0.79)
        Label(self.window, font = ("Arial bold", 7), justify = "left",
              text = "W : Look Up\n\nS : Look Down\n\nA : Look Left\n\nD : Look Right",
              width = len(" Camera Control "),
              fg = "#00e6b8",
              bg = "black").place(relx = 0.0, rely = 0.73)

        Label(self.window, font = ("Courier bold", 12), text = "Camera Control", width = len(" Camera Control "),
              fg = "white",
              bg = "black").place(relx = 0.132 + 0.04, rely = 0.89)

    def CreateMovementButton(self):

        self.MoveForward = Button(self.window, font = ("Courier bold", 16), text = "\u2191", width = 4,
                                  bg = "black",
                                  fg = "red",
                                  borderwidth = 0, highlightthickness = 0, activebackground = "black",
                                  activeforeground = "white")
        self.MoveForward.place(relx = 0.675, rely = 0.72)
        self.MoveBackward = Button(self.window, font = ("Courier bold", 16), text = "\u2193", width = 4,
                                   bg = "black",
                                   fg = "red",
                                   borderwidth = 0, highlightthickness = 0, activebackground = "black",
                                   activeforeground = "white")
        self.MoveBackward.place(relx = 0.675, rely = 0.8)
        self.TurnLeft = Button(self.window, font = ("Courier bold", 16), text = "\u2190", width = 4,
                               bg = "black",
                               fg = "red",
                               borderwidth = 0, highlightthickness = 0, activebackground = "black",
                               activeforeground = "white")
        self.TurnLeft.place(relx = 0.6, rely = 0.8)
        self.TurnRight = Button(self.window, font = ("Courier bold", 16), text = "\u2192", width = 4,
                                bg = "black",
                                fg = "red",
                                borderwidth = 0, highlightthickness = 0, activebackground = "black",
                                activeforeground = "white")
        self.TurnRight.place(relx = 0.75, rely = 0.8)
        Label(self.window, font = ("Arial bold", 7), justify = "left",
              text = "Up Key : Forward\n\nDown Key : Back\n\nLeft Key : Left\n\nRight Key : Right",
              width = len(" Camera Control "),
              fg = "#00e6b8",
              bg = "black").place(relx = 0.82, rely = 0.73)#change value

        Label(self.window, font = ("Courier bold", 12), text = "Motion Control", width = len(" Camera Control "),
              fg = "white",
              bg = "black").place(relx = 0.6, rely = 0.89)


if __name__ == "__main__":
    RcModeController().StreamScreen()
