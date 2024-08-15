from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=50)
print(input.get())
input.grid(row=2, column=3)

















window.mainloop()