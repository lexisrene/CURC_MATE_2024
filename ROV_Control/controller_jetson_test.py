# MATE ROV 2022 Competition

# Receives input from controller (currently configured for Xbox X controller) and translates the input into
# output values for 6 motors in vector drive

# Uses pygame to handle controller input, and sends the values for the motors in an array to the arduino serial

import pygame
from pygame import *
import numpy
import serial
from serial import Serial
from adafruit_servokit import ServoKit



class Controller:

	def __init__(self):
		# setting up pygame stuff
		pygame.init()
		pygame.display.set_caption('ROV')
		pygame.joystick.init()
		self.screen = pygame.display.set_mode([30,30])
		self.clock = pygame.time.Clock()

		# setting up arduino object to send serial comms 
		self.kit = ServoKit(channels=16, address=0x40)
		self.done = False

		# mapping buttons for xbox x controller
		self.LEFT_HORI = 0
		self.RIGHT_HORI = 3
		self.LEFT_VERT = 1
		self.RIGHT_VERT = 4

		self.LEFT_BUMPER = 2
		self.RIGHT_BUMPER = 3

		self.LEFT_TRIGGER = 2
		self.RIGHT_TRIGGER = 5
		self.A= 0
		self.B = 1   

		# default value for when motor is off
		self.STOP_VAL = 0
		self.pos = 0
		self.light = 0

		# initializing each of the motors
		self.reset()

		# array of values for the motor to be passed over to the arduinp
		self.motor_arr = [self.MOTORAB, self.MOTORDF, self.MOTORC, self.MOTORE, self.cur_grip, self.pos, self.light]

	def move(self):
		while not self.done:
			self.screen.fill([0, 0, 0])

			# reset the motors to off-state when no input from controller
			self.reset()

			# exit pygame window to quit loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True

			# initialize joystick
			joy = pygame.joystick.Joystick(0)
			joy.init()


			# set up axis responsible for up/down, fwd/bkwd, rotating, and strafing
			self.UD_axis = joy.get_axis(self.LEFT_VERT)
			self.FB_axis = joy.get_axis(self.RIGHT_VERT)
			self.rot = joy.get_axis(self.RIGHT_HORI)
			self.open = joy.get_axis(self.LEFT_TRIGGER)
			self.close = joy.get_axis(self.RIGHT_TRIGGER)


			self.hori = joy.get_button(self.A)
			self.vert = joy.get_button(self.B)
			self.dim = joy.get_button(self.LEFT_BUMPER)
			self.bright = joy.get_button(self.RIGHT_BUMPER)

			# send axis positions to be evaluated for motor values
			self.motor_vector(self.UD_axis, self.FB_axis, self.rot, self.open, self.close)

			self.servos(self.hori, self.vert, self.dim, self.bright)

			# sends values to the arduino 
			self.send_ada(self.motor_arr)



			print(self.motor_arr)

			self.clock.tick(60)



	def motor_vector(self, UP, FB, rot,  open, close):
		# if the left vertical axis is activated, map the value and send the same value to the up/down motors
		if(UP > 0.1 or UP < -0.1):
			UD_val = (UP+1) /2 *(0.2 - (-0.2)) -0.2
			FB_val = (FB+1) /2 *(0.4 - (-0.4)) -0.4
			self.MOTORAB = UD_val 
			self.MOTORDF = UD_val * 2.7
			self.MOTORC = FB_val
			self.MOTORE = FB_val

			self.cur_grip = self.STOP_VAL

		# if the right vert axis is activated, map the value and send the same value to all 4 horizontal motors
		if(FB > 0.1 or FB < -0.1):
			UD_val = (UP+1) /2 *(0.2 - (-0.2)) -0.2
			FB_val = (FB+1) /2 *(0.4 - (-0.4)) -0.4

			self.MOTORAB = UD_val 
			self.MOTORDF = UD_val * 2.7
			self.MOTORC = FB_val
			self.MOTORE = FB_val

			self.cur_grip = self.STOP_VAL
		if(rot >0.1 or rot < -0.1):
			UD_val = (UP+1) /2 *(0.2 - (-0.2)) -0.2
			LR2_val = (rot + 1) / 2 * (0.2 - (-0.2)) - 0.2
			LR1_val = -LR2_val

			self.MOTORAB = UD_val
			self.MOTORDF = UD_val
			self.MOTORC = LR1_val
			self.MOTORE = LR2_val

			self.cur_grip = self.STOP_VAL
		if(open >0.1 or close > 0.1):
			claw = (close - open + 1) / 2 * (0.05 - (-0.05)) - 0.05

			self.MOTORAB = self.STOP_VAL
			self.MOTORDF = self.STOP_VAL
			self.MOTORC = self.STOP_VAL
			self.MOTORE = self.STOP_VAL
			
			self.cur_grip = claw

			
		

		# continuously updates the motor values in the array
		self.motor_arr = [self.MOTORAB, self.MOTORDF, self.MOTORC, self.MOTORE, self.cur_grip, self.pos, self.light]

	def servos(self, hori, vert, dim, bright):
		if hori == 1:
			self.pos = 180
		if vert == 1:
                    self.pos = 0
		if dim == 1:
                    self.light = 90
		if bright == 1:
                    self.light = 0


		self.motor_arr = [self.MOTORAB, self.MOTORDF, self.MOTORC, self.MOTORE, self.cur_grip, self.pos, self.light]




	def send_ada(self, values):
		# converts motor value array to string to send to arduino
		print(values)
		# thrusters
		self.kit.continuous_servo[2].throttle = values[0]
		self.kit.continuous_servo[3].throttle = values[1]
		self.kit.continuous_servo[4].throttle = values[2]
		self.kit.continuous_servo[5].throttle = values[3]
		# claw
		self.kit.continuous_servo[1].throttle = values[4]		
		# servo
		self.kit.servo[0].set_pulse_width_range(min_pulse=500, max_pulse=2500)
		self.kit.servo[0].angle = values[5]
		self.kit.servo[6].set_pulse_width_range(min_pulse=1100, max_pulse=1900)
		self.kit.servo[6].angle = values[6]




	def reset(self):
		#sets the motors to off position
		self.MOTORAB = self.STOP_VAL
		self.MOTORDF = self.STOP_VAL
		self.MOTORC = self.STOP_VAL
		self.MOTORE = self.STOP_VAL
		self.cur_grip = self.STOP_VAL


controller = Controller()
controller.move()
