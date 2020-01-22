import os
from time import sleep

from MessageBox import messagebox
from settings import Settings
from SystemTest import *
from TkinterCam import *
from UpdateConsole import Updates


class Console:
    window = ""
    radio_var = 0
    radio_buttons_labels_vals = { 1: ["Manual Operation Mode ",
                                      "Operate Visior  with keyboard by controlling\n- Camera Movment\n- Movment of the Bot \n- Monitoring sensor data",
                                      1],
                                  2: ["Autonomous  mode",
                                      "Operate Visior in self controlled mode  \n- Provide the source and destination to Bot",
                                      2],
                                  3: ["Scan VISIOR Components",
                                      "Inspect & 'TroubleShoot' \nThe Sensors and modules onboard Visior \n Before Starting Mission",
                                      3] }
    radio_buttton_vars = [0, 0, 0]
    radio_button_clicked = -1

    def removeUpdateFile(self):
        UpdateFolder = "VisiorNewUpdates"
        if os.path.exists(UpdateFolder):
            os.system('rmdir /S /Q "{}"'.format(UpdateFolder))
            print("Removed Update File by Console.py ...")
        else:
            print("Prevoius Update File Not Found .. ")
            pass

    def __init__(self):
        self.removeUpdateFile()
        settings_ = Settings()
        self.window = Tk()
        self.window.geometry(settings_.getResolution())
        self.window.config(bg = settings_.getBgColor())

        self.window.overrideredirect(
            settings_.isOverRideAlloweded())  # if plf.system().lower() == 'windows' else self.window.wm_attributes("-type","splash")
        self.window.resizable(0, 0)
        self.window.geometry(f"+{abs(0)}+{abs(0)}")
        for i in range(10):
            self.radio_buttton_vars.append(0)

        self.window.focus_set()

        Button(self.window, font = ("Courier bold", 10), text = "\u274c", command = self.window.destroy, width = 4,
               bg = "black",
               fg = "red",
               borderwidth = 0, highlightthickness = 0, activebackground = "black",
               activeforeground = "white").place(relx = 0.91, rely = 0.0)

        # Button(self.window, font = ("Cambria bold", 11), text = "Check Updates", command = self.CheckUpdates, width = 11,
        #         fg = "#2ade2a", bg = "black",
        #        borderwidth = 3, highlightthickness = 0, activebackground = "black",
        #        activeforeground = "white",relief="ridge").place(relx = 0.63, rely = 0.93)

        self.radio_buttton_vars.clear()
        print("Console MainMenu Creating Call")
        self.MainMenu()

    def MainMenu(self):
        try:
            self.radio_button_clicked = -1
            i = 0
            y_pos = 0.2
            self.radio_var = IntVar()

            for indexes, values in self.radio_buttons_labels_vals.items():
                Radiobutton(self.window, text = values[0], variable = self.radio_var, value = values[-1], bg = "black",
                            fg = "red", font = ("Cambria bold ", 11), borderwidth = 0, highlightthickness = 0,
                            command = lambda: self.SetRadioClicked(self.radio_var.get()), activebackground = "black",
                            activeforeground = "white").place(relx = 0.2, rely = y_pos)
                Label(self.window, text = values[1], bg = "black", fg = "#00e6b8", font = ("Courier ", 10),
                      justify = "left").place(relx = 0.2, rely = y_pos + 0.055)
                i += 1
                y_pos += 0.27

            Button(self.window, font = ("Cambria bold", 11), text = "Proceed", width = 10, fg = "#00e6b8", bg = "black",
                   borderwidth = 3, highlightthickness = 0, command = self.callDecider, activebackground = "black",
                   activeforeground = "white", relief = "ridge").place(relx = 0.83, rely = y_pos - 0.08)

            Button(self.window, font = ("Cambria bold", 11), text = "Check Updates", command = self.CheckUpdates,
                   width = 11,
                   fg = "#2ade2a", bg = "black",
                   borderwidth = 3, highlightthickness = 0, activebackground = "black",
                   activeforeground = "white", relief = "ridge").place(relx = 0.02, rely = 0.93)

            # Label(self.window, text = "Select any option and click 'Next' to proceed", bg = "black", fg = "red",
            #       font = ("Courier ", 10), justify = "left").place(relx = 0.05, rely = y_pos - 0.08)
            self.createHeader()
            print("Console MainMenu Creating  Done  ...")
            self.window.mainloop()
        except Exception as e:
            print(f"Exception in <Function> MainMenu - <Class> Console - <File> Console.py --> {e}")
            pass

    def SetRadioClicked(self, radio_val):
        self.radio_button_clicked = radio_val

    def callDecider(self):
        if self.radio_button_clicked == 1:
            self.RcMode()
        elif self.radio_button_clicked == 2:
            pass
        elif self.radio_button_clicked == 3:
            self.sysTest()
        elif self.radio_button_clicked == -1:
            messagebox("Error", "No Option Selected")

    def RcMode(self):
        try:
            if self.window:
                self.window.destroy()
                print("Jumped to TkinterCam  from Console .. ")
                RcModeController().StreamScreen()
        except Exception as e:
            print(f"Exception in <Function> RcMode - <Class> Console - <File> Console.py --> {e}")
            pass

    def sysTest(self):
        try:
            if self.window:
                self.window.destroy()
                print("Jumped to System Test  from Console .. ")
                SystemTest()
        except Exception as e:
            print(f"Exception in <Function> sysTest - <Class> Console - <File> Console.py --> {e}")
            pass

    def createHeader(self):
        i = 0
        j = 1.0
        name_list = ["V ", "I ", "S ", "I", "O ", "R"]
        last_val = 0.25
        while i <= 5:
            while (j >= last_val):
                header_label = Label(self.window, text = name_list[i], bg = "black", fg = "#2ade2a",
                                     font = ("Courier ", 20))

                cover_label = Label(self.window, text = "\t", bg = "black", fg = "black", font = ("Courier ", 20))

                header_label.place(relx = j, rely = 0.04)
                cover_label.place(relx = j + 0.07, rely = 0.04)
                j -= 0.07
                # j=last_val

                self.window.update()
                # sleep(0.01711)
            j = 1.0
            last_val += 0.07
            i += 1
        sleep(0.2)
        Label(self.window, text = "C o n t r o l    P a n e l", bg = "black", fg = "#2ade2a",
              font = ("Courier ", 15)).place(relx = 0.35, rely = 0.12)

    def CheckUpdates(self):
        # CreateUpdate()
        self.window.destroy()
        Updates().CheckUpdate()

    def __del__(self):
        pass


if __name__ == "__main__":
    Console()
