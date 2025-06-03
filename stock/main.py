import tkinter as tk
from tkinter import messagebox
import pandas as pd


def show_prices():
    df = pd.read_csv('Dow Jones Stocks February.csv')
    df = df.drop(columns=["Date"])

    high_low = df.agg(['max', 'min']).transpose().reset_index()
    high_low.columns = ['Stock', 'High Price', 'Low Price']

    message_lines = []
    for _, row in high_low.iterrows():
        message_lines.append(f"{row['Stock']}: High = {row['High Price']:.2f}, Low = {row['Low Price']:.2f}")

    message = "\n".join(message_lines)
    messagebox.showinfo("February High / Low Prices", message)


root = tk.Tk()
root.title("Dow Jones Stock Price Viewer")

btn = tk.Button(root, text="Show February High/Low Prices", width=30, height=2, command=show_prices)
btn.pack(pady=20, padx=20)

root.mainloop()