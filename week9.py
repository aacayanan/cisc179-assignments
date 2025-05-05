import tkinter as tk

mpg = 0


def calculate_gallon():
    global mpg
    try:
        miles = float(miles_input.get())
        gallons = float(gallon_input.get())
        mpg = round(miles / gallons, 2)
    except ValueError:
        mpg = "Invalid input"
    gallon_mpg.config(text=f"{mpg}")


# create main window
root = tk.Tk()
root.title("Gas Mileage Calculator")
root.geometry("420x400")

# top label
main_label = tk.Label(root, text="Gas Mileage Calculator", font=("Arial", 20))
main_label.pack(pady=10)

# input frame
input_frame = tk.Frame(root)

# gallons input field
gallon_frame = tk.Frame(input_frame)
gallon_label_frame = tk.Frame(gallon_frame)
gallon_label = tk.Label(gallon_label_frame, text="Max Gallons:", font=("Arial", 12))
gallon_input = tk.Entry(gallon_frame, font=("Arial", 12))
gallon_label.pack(side=tk.LEFT)
gallon_label_frame.pack(side=tk.TOP, pady=5, fill=tk.X)
gallon_input.pack(side=tk.BOTTOM, pady=5)
gallon_frame.pack(pady=10, side=tk.LEFT, padx=5)

# miles driven input field
miles_frame = tk.Frame(input_frame)
miles_label_frame = tk.Frame(miles_frame)
miles_label = tk.Label(miles_label_frame, text="Total Miles:", font=("Arial", 12))
miles_input = tk.Entry(miles_frame, font=("Arial", 12))
miles_label.pack(side=tk.LEFT)
miles_label_frame.pack(side=tk.TOP, pady=5, fill=tk.X)
miles_input.pack(side=tk.BOTTOM, pady=5)
miles_frame.pack(pady=10, side=tk.RIGHT, padx=5)
input_frame.pack(pady=10)

# calculate button
calculate = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_gallon)
calculate.pack(pady=10)

# line across the screen
line = tk.Frame(root, height=1, bg="gray")
line.pack(fill=tk.X, pady=5)

# miles per gallon mpg field
gallon_mpg_frame = tk.Frame(root)
gallon_mpg_label_frame = tk.Frame(gallon_mpg_frame)
gallon_mpg_label = tk.Label(gallon_mpg_label_frame, text="Miles per Gallon:", font=("Arial", 12))
gallon_mpg = tk.Label(gallon_mpg_frame, text=f"{mpg}", font=("Arial", 12))
gallon_mpg_label.pack(side=tk.LEFT)
gallon_mpg_label_frame.pack(side=tk.TOP, pady=5, fill=tk.X)
gallon_mpg.pack(side=tk.BOTTOM, pady=5)
gallon_mpg_frame.pack(pady=10)

# start program
root.mainloop()
