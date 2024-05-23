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

orders = []

class Ticket:
    def __init__(self) -> None:
        self.Adults = 0
        self.Children = 0
        self.Concession = 0
    
    def __str__(self) -> str:
        msg = f'''Tickets:
Adults: {self.Adults}
Children: {self.Children}
Concession: {self.Concession}'''
        return msg
    
    def update_tickets(self) -> None:
        self.Adults = info["Adult"]["Input"].get()
        self.Children = info["Child"]["Input"].get()
        self.Concession = info["Concession"]["Input"].get()
        print(info["Concession"]["Input"].get())
    
    def total_price(self) -> int:
        total = 0
        total += self.Adults * info["Adult"]["Price"]
        total += self.Children * info["Child"]["Price"]
        total += self.Concession * info["Concession"]["Price"]
        return total
    
    def save_order(self) -> None:
        orders.append(self)
        info["Adult"]["Total"] += self.Adults
        info["Child"]["Total"] += self.Children
        info["Concession"]["Total"] += self.Concession

root.mainloop()