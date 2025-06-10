import tkinter as tk
from tkinter import font
import random

root = tk.Tk()
root.title('Chance simulator')
root.geometry("800x800")
Font = font.Font(family="Arial", size=32)
smolFont = font.Font(family="Arial", size=16)
storedNumber = 0

# funktions
def on_change(*args):
    value = var.get()
    try:
        value = float(value)
        if value > 100:
            var.set('100')
        elif value < 0:
            var.set('0')
        if not (0 <= value <= 100):
            var.set(''.join(c for i, c in enumerate(value) if c.isdigit() or (c == '.' and '.' not in value[:i])))
    except ValueError:
        pass
def on_submit():
    global RealstoredNumber
    RealstoredNumber = var.get()
    if var.get() == '':
        stored_number.config(text=f"Stored chance: NaN%")
    else:
        stored_number.config(text=f"Stored chance: {RealstoredNumber}%")
    greenScore.config(text="0")
    redScore.config(text="0")
    try_button.pack()
    state_label.pack()
    Frame2.pack(pady=Padding)
    resetButton.pack()
def calculate():
    value = float(RealstoredNumber)
    random_float = round(random.uniform(0, 100), 1)
    if random_float <= value:
        greenScore.config(text=str(int(greenScore.cget("text")) + 1))
        state_label.config(text="Event success!", fg="green")
    else:
        redScore.config(text=str(int(redScore.cget("text")) + 1))
        state_label.config(text="Event fail!", fg="red")
def reset():
    var.set('')
    Frame2.pack_forget()
    resetButton.pack_forget()
    try_button.pack_forget()
    state_label.pack_forget()
    storedNumber = "NaN"
    RealstoredNumber = 0
    stored_number.config(text=f"Stored chance: NaN%")
var = tk.StringVar()
var.trace_add("write", on_change)
Padding = 10
# Screen
Instruction = tk.Label(root, text="Chance of event occurring:", font=Font)
state_label = tk.Label(root, text="Click 'Run'", font=Font, pady=Padding)
try_button = tk.Button(root, text="Run", font=Font, command=calculate, pady=Padding, bd=8, relief="raised")
submit_button = tk.Button(root, text="Enter", font=Font, command=on_submit, bd=8, relief="raised")
stored_number = tk.Label(root, text="Stored chance: NaN%", font=smolFont)
resetButton = tk.Button(root, text="Reset", font=Font, pady=Padding, command=reset, bd=8, relief="raised")
# FRAME 1
Frame1 = tk.Frame(root)

Entry = tk.Entry(Frame1, width=5, textvariable=var, font=Font)
percent_label = tk.Label(Frame1, text="%", font=Font)


# FRAME 2
Frame2 = tk.Frame(root)

greenScore = tk.Label(Frame2, text="0", font=Font, pady=Padding, fg="green")
redScore = tk.Label(Frame2, text="0", font=Font, pady=Padding, fg="red")
dashScore = tk.Label(Frame2, text="-", font=Font, pady=Padding)


# Rendering
# Rendering -> Frame1
Entry.grid(row=1, column=0, pady=Padding)
percent_label.grid(row=1, column=1, pady=Padding)
# Rendering -> Frame 2
greenScore.grid(row=2, column=0)
dashScore.grid(row=2, column=1)
redScore.grid(row=2, column=2)
# Rendering Frames and Screen
Instruction.pack(pady=Padding)
Frame1.pack(pady=Padding)
submit_button.pack()
stored_number.place(x=50, y=200)
root.mainloop()