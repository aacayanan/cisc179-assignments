import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x100")
# create the title label
title_label = tk.Label(root, text="Enter Actual Property Value:")
title_label.pack(pady=10)
# create the entry field
entry = tk.Entry(root)
entry.pack()


def on_submit():
    entry_value = entry.get()
    # check if entry is empty
    if not entry_value:
        messagebox.showerror("Error", "Please enter a value.")
        return
    assessment_value = (float(entry_value) * 0.6)
    property_tax = ((float(assessment_value) / 100) * 0.75)
    assessment_value = "{:.2f}".format(round(assessment_value, 2))
    property_tax = "{:.2f}".format(round(property_tax, 2))
    # create info dialog box
    tk.messagebox.showinfo(
        "Property Assessment",
        f"Your assessment value is: ${assessment_value}\n"
        f"Your property tax is: ${property_tax}",
    )


# submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=5)

root.mainloop()