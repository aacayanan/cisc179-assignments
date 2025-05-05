import tkinter as tk


class Week12:
    def __int__(self):
        self.main_window = tk.Tk()

        self.label = tk.Label(self.main_window, text="Programming is fun!")
        self.label.pack()

        self.main_window.mainloop()


app = Week12()
