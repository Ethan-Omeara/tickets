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

current_order = Ticket()
total = StringVar(root, "$0")

def update_total(*args):
    current_order.update_tickets()
    total.set("$" + str(current_order.total_price()))

def submit(*args):
    global current_order
    current_order.update_tickets()
    current_order.save_order()
    current_order = Ticket()
    total.set(0)
    info["Adult"]["Input"].set(0)
    info["Child"]["Input"].set(0)
    info["Concession"]["Input"].set(0)
    print(orders[0])
    print(orders[1])

info["Adult"]["Input"].trace_add('write', update_total)
info["Child"]["Input"].trace_add('write', update_total)
info["Concession"]["Input"].trace_add('write', update_total)

Label(root, text="Adults").grid(row=0, column=0)
Label(root, text="Children").grid(row=1, column=0)
Label(root, text="Concession").grid(row=2, column=0)
Label(root, text="Total", font=('Arial', 12, "bold")).grid(row=3, column=0)

Entry(root, textvariable=info["Adult"]["Input"]).grid(row=0, column=1)
Entry(root, textvariable=info["Child"]["Input"]).grid(row=1, column=1)
Entry(root, textvariable=info["Concession"]["Input"]).grid(row=2, column=1)
Label(root, textvariable=total).grid(row=3, column=1)

Button(root, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)

root.mainloop()