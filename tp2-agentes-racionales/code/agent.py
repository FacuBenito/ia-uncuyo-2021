from environment import *

class Agent:
	actions = 1000

	def __init__(self, env):
		self.env = env

	def up(self):
		env = self.env

		if(env.currentPosY > 0):
			env.currentPosY = env.currentPosY - 1
			self.actions = self.actions - 1
	
	def down(self):
		env = self.env

		if(env.currentPosY < len(env.matrix) - 1):
			env.currentPosY = env.currentPosY + 1
			self.actions = self.actions - 1
	
	def left(self):
		env = self.env

		if(env.currentPosX > 0):
			env.currentPosX = env.currentPosX - 1
			self.actions = self.actions - 1

	def right(self):
		env = self.env

		if(env.currentPosX < len(env.matrix) - 1):
			env.currentPosX = env.currentPosX + 1
			self.actions = self.actions - 1

	def suck(self):
		env = self.env
		matrix = env.matrix

		matrix[env.currentPosY][env.currentPosX] = 0
		self.actions = self.actions - 1

	def idle(self):
		self.actions = self.actions - 1

	def perspective(self, env):
		if(env.isDirty()):
			self.suck()
		else:
			self.idle()

	def think(self):
		# Please comment lines 55, ..., 63 and uncomment lines 67, ..., 70 for excercise E
		self.perspective(self.env)

		possibleDirections = [
			'up', 'down', 'left', 'right'
		]

		direction = possibleDirections[randint(0,3)]
		callback = getattr(self, direction)
		self.env.acceptAction(callback)

		# -- The code below is for the fully random agent excercise! --

		# possibleActions = ['up', 'down', 'left', 'right', 'suck', 'idle']
		# action = possibleActions[randint(0,5)]
		# callback = getattr(self, action)
		# self.env.acceptAction(callback)
