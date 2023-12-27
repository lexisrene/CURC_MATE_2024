import tkinter as tk
from PIL import Image, ImageTk
import countdown

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CURC ROV 2024")

        # Fullscreen settings
        self.root.attributes('-fullscreen', True)
        self.root.minsize(800, 500)

        # Bind keys for fullscreen toggle and quit
        self.root.bind("<Escape>", self.end_fullscreen)
        self.root.bind("<Control-c>", lambda event: self.root.quit())

        # Layout configuration
        self.configure_layout()

        # Load and display logo
        self.display_logo()

        self.display_navbar_buttons()

        # Setup and display countdown widget
        self.setup_countdown()

    def configure_layout(self):
        window_width = self.root.winfo_width()

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=15)
        self.root.rowconfigure(0, weight=1)

        self.navBar = tk.Frame(self.root, background='#75aadb')
        self.navBar.config(width=window_width * 0.1)
        self.main = tk.Frame(self.root, background='white')

        self.navBar.grid(row=0, column=0, sticky='nsew')
        self.main.grid(row=0, column=1, sticky='nsew')

        self.main.columnconfigure((0, 1, 2), weight=1)
        self.main.rowconfigure((0, 1), weight=3)
        self.main.rowconfigure(2, weight=1)

    def display_logo(self):
        curc_logo_original = Image.open('images/curc_logo_color.png').convert('RGB').resize((90, 90))
        curc_logo = ImageTk.PhotoImage(curc_logo_original)

        logo_label = tk.Label(self.navBar, image=curc_logo, background='#75aadb')
        logo_label.image = curc_logo  # Keep a reference!
        logo_label.pack(side='top', pady=20)

    def display_navbar_buttons(self):
        btn_one = tk.Button(self.navBar, text='One', bd='5', highlightbackground="#75aadb")
        btn_one.pack(side='top', pady=(80, 30))

        btn_two = tk.Button(self.navBar, text='Two', bd='5', highlightbackground="#75aadb")
        btn_two.pack(side='top', pady=30)

        btn_three = tk.Button(self.navBar, text='Three', bd='5', highlightbackground="#75aadb")
        btn_three.pack(side='top', pady=30)

        btn_four = tk.Button(self.navBar, text='Four', bd='5', highlightbackground="#75aadb")
        btn_four.pack(side='top', pady=30)

        btn_five = tk.Button(self.navBar, text='Five', bd='5', highlightbackground="#75aadb")
        btn_five.pack(side='top', pady=30)

    def setup_countdown(self):
        countdown_frame = tk.Frame(self.main, background='white')
        countdown_grid = tk.Frame(countdown_frame)
        countdown_grid.columnconfigure((0, 1), weight=1)
        countdown_grid.rowconfigure(0, weight=1)
        countdown_grid.pack(side='top')

        countdown_frame.grid(row=2, column=0, sticky=tk.SW, padx=40, pady=40)

        self.countdown_widget = countdown.Countdown(countdown_grid, 15, 0)
        start_btn = tk.Button(countdown_frame, text='START', bd='5', highlightbackground='white', command=lambda: self.countdown_widget.startCount(15*60))
        start_btn.pack(side='top')

    def end_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)


if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
