"""This file is a ticket ordering system with a GUI."""

# Import libraries, initialise constants
from tkinter import *
root = Tk()
NUMBERS = '0123456789'


def get_int(self: StringVar) -> int:
    """Return an integer from a StringVar."""
    current_entry = self.get()
    new_entry = ''
    # Remove characters
    for char in current_entry:
        if char in NUMBERS:
            new_entry += char

    # Convert to integer
    try:
        new_entry = int(new_entry)
    except ValueError:
        new_entry = 0

    self.set(str(new_entry))
    return new_entry


# Hijacking the StringVar class to make number processing easier
StringVar.get_int = get_int
StringVar.set_int = lambda self, value: self.set(str(value))

# ===================================================

# Create info global
info = {
    "Adult": {
        "Price": 15,
        "Total": 0,
        "Input": StringVar(root, "0")
    },
    "Child": {
        "Price": 5,
        "Total": 0,
        "Input": StringVar(root, "0")
    },
    "Concession": {
        "Price": 10,
        "Total": 0,
        "Input": StringVar(root, "0")
    },
}

# ==============
# Define classes
# ==============


class Ticket:
    """Class to represent an order of tickets."""

    def __init__(self) -> None:
        """Initialise Ticket class."""
        self.Adults = 0
        self.Children = 0
        self.Concession = 0

    def __str__(self) -> str:
        """Return the ticket data in a string format."""
        msg = f'''Tickets:
Adults: {self.Adults}
Children: {self.Children}
Concession: {self.Concession}'''
        return msg

    def update_tickets(self) -> None:
        """Update the ticket data from entry boxes."""
        self.Adults = info["Adult"]["Input"].get_int()
        self.Children = info["Child"]["Input"].get_int()
        self.Concession = info["Concession"]["Input"].get_int()

    def total_price(self) -> int:
        """Return the total price of tickets in the order."""
        total = 0
        total += self.Adults * info["Adult"]["Price"]
        total += self.Children * info["Child"]["Price"]
        total += self.Concession * info["Concession"]["Price"]
        return total

    def save_order(self) -> None:
        """Save the order and update total tickets."""
        orders.append(self)
        info["Adult"]["Total"] += self.Adults
        info["Child"]["Total"] += self.Children
        info["Concession"]["Total"] += self.Concession


# ====================
# Define other globals
# ====================

orders = []
current_order = Ticket()
total = StringVar(root, "$0")

# ================
# Define functions
# ================


def update_total(*args) -> None:
    """Update the ticket class and set the total StringVar."""
    current_order.update_tickets()
    total.set("$" + str(current_order.total_price()))


def submit(*args) -> None:
    """Submit order and reset GUI."""
    global current_order
    current_order.update_tickets()
    current_order.save_order()
    current_order = Ticket()
    total.set(0)
    info["Adult"]["Input"].set_int(0)
    info["Child"]["Input"].set_int(0)
    info["Concession"]["Input"].set_int(0)


# Attach functions for when entry boxes are updated
info["Adult"]["Input"].trace_add('write', update_total)
info["Child"]["Input"].trace_add('write', update_total)
info["Concession"]["Input"].trace_add('write', update_total)

# Create GUI and attach appropriate textvariables
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
