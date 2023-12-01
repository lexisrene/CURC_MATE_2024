import tkinter as tk
import PIL
from PIL import Image, ImageTk
import countdown

# Create the main window
root = tk.Tk()
root.title("CURC ROV 2024")

# Set the window to full screen
root.attributes('-fullscreen', True)
root.minsize(800, 500)

# If you want to allow toggling fullscreen mode on and off with a key (e.g., F11)

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root.bind("<Escape>", end_fullscreen)
root.bind("<Control-c>", lambda event: root.quit())

window_width = root.winfo_width()
window_height = root.winfo_height()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=15)
root.rowconfigure(0, weight=1)

curc_logo_original = Image.open('images/curc_logo_color.png').convert('RGB').resize((90, 90))
curc_logo = ImageTk.PhotoImage(curc_logo_original)


navBar = tk.Frame(root, background='#75aadb')
navBar.config(width=window_width * 0.1)
main = tk.Frame(root, background='white')
navBar.grid(row=0, column=0, sticky='nsew')
main.grid(row=0, column=1, sticky='nsew')
main.columnconfigure((0, 1, 2), weight=1)
main.rowconfigure((0, 1), weight=3)
main.rowconfigure(2, weight=1)

logo_label = tk.Label(navBar, image=curc_logo, background='#75aadb')
logo_label.pack(side='top', pady = 20)

countdown_frame = tk.Frame(main, background='white')
countdown_grid = tk.Frame(countdown_frame)
countdown_grid.columnconfigure((0, 1), weight=1)
countdown_grid.rowconfigure(0, weight=1)
countdown_grid.pack(side='top')
countdown_frame.grid(row = 2, column=0, sticky=tk.SW, padx = 40, pady = 40)
countdown_widget = countdown.Countdown(countdown_grid, 15, 0)
start_btn = tk.Button(countdown_frame, text='START', bd='5', highlightbackground='white', command=lambda: countdown_widget.startCount(15*60))
start_btn.pack(side='top')

root.mainloop()
