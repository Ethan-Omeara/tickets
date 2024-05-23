from tkinter import *

root = Tk()

info = {
    "Adult": {
        "Price": 15,
        "Total": 0,
        "Input": IntVar()
    },
    "Child": {
        "Price": 5,
        "Total": 0,
        "Input": IntVar()
    },
    "Concession": {
        "Price": 10,
        "Total": 0,
        "Input": IntVar()
    },
}

root.mainloop()