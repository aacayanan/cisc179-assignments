import tkinter as tk
from tkinter import Radiobutton, messagebox

# radiobutton options
options = {
    "Daytime (6:00 a.m. through 5:59 p.m.)": 0.07,
    "Evening (6:00 p.m. through 11:59 p.m.)": 0.12,
    "Off-Peak (midnight through 5:59 a.m.)": 0.05,
}

# create the main window
root = tk.Tk()
root.geometry("300x200")

# create the title label
title_label = tk.Label(root, text="Select a time period:")
title_label.pack()

v = tk.DoubleVar()
# create the buttons
for (text, value) in options.items():
    Radiobutton(root, text=text, variable=v, value=value).pack()

# enter value
entry_label = tk.Label(root, text="Enter minutes:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()


def on_submit():
    selected_option = v.get()
    entry_value = entry.get()
    rate = selected_option * float(entry_value)
    rate = round(rate, 2)
    # create info dialog box
    messagebox.showinfo(
        "Rate",
        f"Your rate is: ${rate}",
    )


# submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=5)

root.mainloop()
