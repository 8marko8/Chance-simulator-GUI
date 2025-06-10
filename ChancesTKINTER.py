import tkinter as tk
from tkinter import font
import random

root = tk.Tk()
root.title("Chance2.py: Number Window")
root.geometry("800x600")
big_font = font.Font(family="Helvetica", size=32)

def on_change(*args):
    value = var.get()
    try:
        float_val = float(value)
        if not (0 <= float_val <= 100):
            raise ValueError
    except ValueError:
        cleaned = ''.join(c for i, c in enumerate(value) if c.isdigit() or (c == '.' and '.' not in value[:i]))
        var.set(cleaned)
        print(f"Deleted character {value}")

Frame2 = tk.Frame(root)
green_score = tk.Label(Frame2, text="0", font=big_font, fg="green")
dash_score = tk.Label(Frame2, text="-", font=big_font)
red_score = tk.Label(Frame2, text="0", font=big_font, fg="red")

def on_submit():
    value = var.get()
    if not (0 <= float(value) <= 100):
        var.set('')
        return
    if float(value) > 100:
        var.set("")
        return
    elif float(value) < 0:
        var.set("")
        return
    button.pack()
    click.pack(pady=20)

frameFirst = tk.Frame(root)
frameFirst.pack(pady=20)
frame = tk.Frame(root)
frame.pack(pady=20)
var = tk.StringVar()
var.trace_add("write", on_change)
label = tk.Label(frameFirst, text="Chance of an event happening", font=big_font)
label.grid(row=0, column=0)
entry = tk.Entry(frame, width=10, textvariable=var, font=big_font)
entry.grid(row=1, column=0)
percent_label = tk.Label(frame, text="%", font=big_font)
percent_label.grid(row=1, column=1)
button_submit = tk.Button(root, text="Submit number", font=big_font, command=on_submit)
button_submit.pack()

def calculate():
    green_score.grid(row=6, column=0)
    dash_score.grid(row=6, column=1)
    red_score.grid(row=6, column=2)
    Frame2.pack(pady=20)
    value = var.get()
    RandNumb = round(random.uniform(0, 100), 1)
    chance = float(value)
    if RandNumb <= chance:
        click.config(text="Event success!", fg="green")
        scoreG = green_score.cget("text")
        green_score.config(text=str(int(scoreG)+1))
        print("Event success")
    else:
        scoreR = red_score.cget("text")
        red_score.config(text=str(int(scoreR)+1))
        click.config(text="Event fail!", fg="red")
        print("Event fail")
        
click = tk.Label(root, text="Click the button.", font=big_font)
button = tk.Button(root, text="Click Me", font=big_font, command=calculate)
root.mainloop()
