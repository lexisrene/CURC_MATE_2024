import tkinter as tk
from tkinter import messagebox

class Countdown:

    def __init__(self, container, minutes, seconds):
        self.container = container
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()
        self.minutes.set("{0:02d}:".format(minutes))
        self.seconds.set("{0:02d}".format(seconds))
        self.mins_label= tk.Label(self.container, textvariable=self.minutes, background='white')
        self.mins_label.config(font=('Courier', 50))
        self.mins_label.grid(column=0, row = 2, sticky=tk.E)
        self.sec_label = tk.Label(self.container, textvariable=self.seconds, background='white')
        self.sec_label.config(font=('Courier', 50))
        self.sec_label.grid(column = 1, row = 2, sticky=tk.W)


    def startCount(self, totalsecs):
        if totalsecs == 0:
            messagebox.showinfo("Alert!", "Time's Up, BOIS")
        
        minutes = totalsecs // 60
        seconds = totalsecs - (minutes * 60)

        self.minutes.set("{0:02d}:".format(minutes))
        self.seconds.set("{0:02d}".format(seconds))

        self.container.after(1000, self.startCount, totalsecs-1)










