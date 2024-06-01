from tkinter import *

#https://www.pygame.org/docs/ref/joystick.html
#Drawing the circles and the color
#We want to change this in order for the to be
#   . .
# .     .
#   . .

class Circles:
    def __init__(self, container):
        self.container = container
    def draw_blue_circles(self):
            global left_circle, right_circle, top_circle, bottom_circle, top_right_circle, top_left_circle, left_intensity, right_intensity, top_intensity, bottom_intensity, top_right_intensity, top_left_intensity

            # Circle to the left
            left_circle = self.container.create_oval(30, 75, 80, 125, fill="lightblue")
            left_intensity = 150  # Start with a lighter color

            # Circle to the right
            right_circle = self.container.create_oval(120, 75, 170, 125, fill="lightblue")
            right_intensity = 150

            # Circle on top
            top_circle = self.container.create_oval(75, 30, 125, 80, fill="lightblue")
            top_intensity = 150

            # Circle on the bottom
            bottom_circle = self.container.create_oval(75, 120, 125, 170, fill="lightblue")
            bottom_intensity = 150

            # Circle on top-right
            top_right_circle = self.container.create_oval(130, 30, 180, 80, fill="lightblue")
            top_right_intensity = 150

            # Circle on top-left
            top_left_circle = self.container.create_oval(30, 30, 80, 80, fill="lightblue")
            top_left_intensity = 150

            return left_circle, right_circle, top_circle, bottom_circle, top_right_circle, top_left_circle, left_intensity, right_intensity, top_intensity, bottom_intensity, top_right_intensity, top_left_intensity

    def on_key_press(self, event):
            global left_intensity, right_intensity, top_intensity, bottom_intensity, top_right_intensity, top_left_intensity

            intensity_step = 10  # Adjust this value to control the step of darkness

            if event.keysym == 'Left':
                left_intensity -= intensity_step
                left_intensity = max(left_intensity, 0)  # Ensure intensity doesn't go below 0
                self.container.itemconfig(left_circle, fill=f"#{left_intensity:02x}{left_intensity:02x}ff")

            elif event.keysym == 'Right':
                right_intensity -= intensity_step
                right_intensity = max(right_intensity, 0)
                self.container.itemconfig(right_circle, fill=f"#{right_intensity:02x}{right_intensity:02x}ff")

            elif event.keysym == 'Up':
                top_intensity -= intensity_step
                top_intensity = max(top_intensity, 0)
                self.container.itemconfig(top_circle, fill=f"#{top_intensity:02x}{top_intensity:02x}ff")

            elif event.keysym == 'Down':
                bottom_intensity -= intensity_step
                bottom_intensity = max(bottom_intensity, 0)
                self.container.itemconfig(bottom_circle, fill=f"#{bottom_intensity:02x}{bottom_intensity:02x}ff")

            elif event.keysym == 'w':
                top_right_intensity -= intensity_step
                top_right_intensity = max(top_right_intensity, 0)
                self.container.itemconfig(top_right_circle, fill=f"#{top_right_intensity:02x}{top_right_intensity:02x}ff")

            elif event.keysym == 'q':
                top_left_intensity -= intensity_step
                top_left_intensity = max(top_left_intensity, 0)
                self.container.itemconfig(top_left_circle, fill=f"#{top_left_intensity:02x}{top_left_intensity:02x}ff")

