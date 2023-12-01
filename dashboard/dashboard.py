import tkinter as tk
import PIL
from PIL import Image, ImageTk

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

curc_logo_original = Image.open('images/curc_logo_color.png').convert('RGB').resize((70, 70))
curc_logo = ImageTk.PhotoImage(curc_logo_original)


navBar = tk.Frame(root, background='#75aadb')
navBar.config(width=window_width * 0.1)
main = tk.Frame(root, background='white')
navBar.grid(row=0, column=0, sticky='nsew')
main.grid(row=0, column=1, sticky='nsew')

logo_label = tk.Label(navBar, image=curc_logo, background='#75aadb')
logo_label.pack(side='top')



root.mainloop()
