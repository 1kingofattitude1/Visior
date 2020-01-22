from tkinter import Tk, Label, Button
from settings import Settings


def messagebox(title, info,font_size = 12):
    settings_ = Settings()

    info_box = Tk()
    info_box.focus_set()
    info_box.geometry(f"+{100}+{100}")

    info_box.geometry("470x270")
    info_box.configure(bg = settings_.getBgColor(), highlightbackground = "white", highlightthickness = 2)
    info_box.resizable(0, 0)
    Button(info_box, font = ("Courier bold", 10), text = "\u274c", command = info_box.destroy, width = 3,
           fg = "red",
           bg = "black",
           borderwidth = 0, highlightthickness = 0, activebackground = "black", activeforeground = "white").place(
        relx = 0.91, rely = 0.01)
    info_box.overrideredirect(settings_.isOverRideAlloweded())

    Label(info_box, text = "\u26A0 " + title, fg = "#2ade2a", bg = "black", font = ("times bold", 14)).pack(
        side = "top", pady = 20)
    Label(info_box, text = info, fg = "#2ade2a", bg = "black", font = ("times bold", font_size), wraplength = 450).pack(
        side = "top",
        pady = 50)

    info_box.mainloop()
