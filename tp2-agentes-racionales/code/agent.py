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
			env.currentPosX = env.currentPosX
			self.actions = self.actions - 1

	def suck(self):
		env = self.env
		matrix = env.matrix

		matrix[env.currentPosY][env.currentPosX] = 0
		self.actions = self.actions - 1

	def idle(self):
		print("Already clean!")

	def perspective(self, env):
		if(env.isDirty()):
			self.suck()
		else:
			self.iddle()



		

		