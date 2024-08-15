from tkinter import *
import math


def miles_to_km():
    miles = float(miles_input.get())
    km = "{:.2f}".format(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Input
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

# Label
miles_label = Label(text="Miles")
miles_label.config(padx=5, pady=5)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.config(padx=5, pady=5)
is_equal_to_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.config(padx=5, pady=5)
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.config(padx=5, pady=5)
kilometer_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate")
button.config(padx=5, pady=5, command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()