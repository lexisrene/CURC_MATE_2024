import tkinter as tk
from PIL import Image, ImageTk
import countdown
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from depth_graphing import *
import motor_status



class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CURC ROV 2024")
        self.xvalues = []
        self.yvalues = []
        self.graph = depth_graphing()
        self.graphs = []
        self.data = []
        self.graphToggle = 0
        self.graphCount = 0

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

        # Buttons in navbar, right now just placeholders
        # add functionality as you see fit
        self.display_navbar_buttons()

        self.depth_graph()

        # Setup and display countdown widget
        self.setup_countdown()

        self.motor_status()

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

    def depth_graph(self):
        test_string = "[31, 00:00:00, 0, 60, 00:00:05, 15, 60, 00:00:10, 30, 60, 00:00:15, 45, 60, 00:00:20, 60, 60, 00:00:25, 75, 60, 00:00:30, 90, 60, 00:00:35, 105, 60, 00:00:40, 120, 60]"

        # have .run return None if no data was received
        # have it return a tuple of (fig, raw_data)
        fig = self.graph.run()
        if fig:
            self.graphs.append(fig[0])
            self.data.append(fig[1])
        if len(self.graphs) > 0:
            self.canvas = FigureCanvasTkAgg(self.graphs[self.graphToggle], master=self.main)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.grid(row=0, column=0, sticky='nw')
            self.canvas.draw()


    
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

    def motor_status(self):
        # motor_frame = tk.Frame(self.main, background='black')
        # motor_frame.pack()
        # Create a canvas widget
        canvas = tk.Canvas(self.main, width=200, height=200)
        status = motor_status.Circles(canvas)
        status.draw_blue_circles()

        # Bind the canvas to the key press event
        canvas.bind('<KeyPress>', status.on_key_press)

        canvas.grid(row=0, column=0)

    def end_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)


if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
