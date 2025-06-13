import tkinter as tk
from tkinter import font
import random
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('Chance simulator')
root.geometry("800x800")
Font = font.Font(family="Arial", size=32)
smolFont = font.Font(family="Arial", size=16)
entryFont = font.Font(family="Arial", size=64)
storedNumber = 0
x = []
list_success = []
list_fails = []
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
    global x, list_success, list_fails
    global RealstoredNumber
    RealstoredNumber = var.get()
    if var.get() == '':
        stored_number.config(text=f"Stored chance: NaN%")
    else:
        stored_number.config(text=f"Stored chance: {RealstoredNumber}%")
    greenScore.config(text="0")
    redScore.config(text="0")
    totalScore.config(text="0")
    try_button.pack()
    state_label.pack()
    Frame2.pack(pady=Padding)
    resetButton.pack()
    Frame3.pack()
    x.clear()
    list_success.clear()
    list_fails.clear()
def calculate():
    global list_success, list_fails
    value = float(RealstoredNumber)
    random_float = round(random.uniform(0, 100), 1)
    if random_float <= value:
        greenScore.config(text=str(int(greenScore.cget("text")) + 1))
        state_label.config(text="Event success!", fg="green")
        print("Success.")
        list_success.append(int(greenScore.cget("text")))
        list_fails.append(int(redScore.cget("text")))
    else:
        redScore.config(text=str(int(redScore.cget("text")) + 1))
        state_label.config(text="Event fail!", fg="red")
        print("Failed.")
        list_fails.append(int(redScore.cget("text")))
        list_success.append(int(greenScore.cget("text")))
    totalScore.config(text=str(int(totalScore.cget("text")) + 1))
    print(f"x: {x}")
    print(f"F: {list_fails}")
    print(f"S: {list_success}")
def reset():
    global x, list_success, list_fails
    var.set('')
    Frame2.pack_forget()
    resetButton.pack_forget()
    try_button.pack_forget()
    state_label.pack_forget()
    Frame3.pack_forget()
    x = []
    list_success = []
    list_fails = []
    storedNumber = "NaN"
    RealstoredNumber = 0
    stored_number.config(text=f"Stored chance: NaN%")
def plot_g():
    global x, list_success
    x = []
    x = [i + 1 for i in range(int(totalScore.cget("text")))]
    plt.plot(x, list_success, label="Plot", color='blue', marker="o")
    plt.xticks(range(min(x), max(x) + 1, 1))
    plt.yticks(range(min(list_success), (max(list_success)) + 1, 1))
    plt.xlabel('Tries')
    plt.ylabel('Successes')
    plt.legend()
    plt.show()
def plot_r():
    global x, list_fails
    x = []
    x = [i + 1 for i in range(int(totalScore.cget("text")))]
    plt.plot(x, list_fails, label="Plot", color='blue', marker="o")
    plt.xticks(range(min(x), max(x) + 1, 1))
    plt.yticks(range(min(list_fails), (max(list_fails)) + 1, 1))
    plt.xlabel('Tries')
    plt.ylabel('Fails')
    plt.legend()
    plt.show()
var = tk.StringVar()
var.trace_add("write", on_change)
Padding = 10
# Screen
Instruction = tk.Label(root, text="Chance of event occurring:", font=Font)
state_label = tk.Label(root, text="Click 'Run'", font=Font, pady=Padding)
try_button = tk.Button(root, text="Run", font=smolFont, command=calculate, pady=Padding, bd=8, relief="raised", height=1)
stored_number = tk.Label(root, text="Stored chance: NaN%", font=smolFont)
resetButton = tk.Button(root, text="Reset", font=smolFont, pady=Padding, command=reset, bd=8, relief="raised", height=1)
# FRAME 1
Frame1 = tk.Frame(root)

Entry = tk.Entry(Frame1, width=5, textvariable=var, font=Font)
percent_label = tk.Label(Frame1, text="%", font=Font)
submit_button = tk.Button(Frame1, text="Enter", font=smolFont, command=on_submit, bd=8, relief="raised", height=1)
# FRAME 2
Frame2 = tk.Frame(root)

greenScore = tk.Label(Frame2, text="0", font=Font, pady=Padding, fg="green")
redScore = tk.Label(Frame2, text="0", font=Font, pady=Padding, fg="red")
totalScore = tk.Label(Frame2, text="0", font=Font, pady=Padding)

# FRAME 3
Frame3 = tk.Frame(root)

plotGreen = tk.Button(Frame3, text="Plot successes over tries", command=plot_g,font=smolFont, pady=Padding, fg="green", bd=8, relief="raised", height=1)
plotRed = tk.Button(Frame3, text="Plot fails over tries", command=plot_r, font=smolFont, pady=Padding, fg="red", bd=8, relief="raised", height=1)
# Rendering
# Rendering -> Frame1
Entry.grid(row=1, column=0, pady=Padding)
percent_label.grid(row=1, column=1, pady=Padding)
submit_button.grid(row=1, column=2, pady=Padding)
# Rendering -> Frame 2
greenScore.grid(row=2, column=0)
totalScore.grid(row=2, column=1)
redScore.grid(row=2, column=2)
# Rendering -> Frame 3
plotGreen.grid(row=0, column=0)
plotRed.grid(row=0, column=1)
# Rendering Frames and Screen
Instruction.pack(pady=Padding)
Frame1.pack(pady=Padding)
stored_number.place(x=50, y=200)
root.mainloop()