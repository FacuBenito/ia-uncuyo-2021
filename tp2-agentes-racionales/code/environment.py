from random import randint

def printMatrix(matrix):
	print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def verifyDirtiness(matrix):
	dirtySlots = 0

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if(matrix[i][j] == 1):
				dirtySlots = dirtySlots + 1

	dirtRate = dirtySlots/(len(matrix[0])**2)
	print("Dirt Rate: ", dirtRate)

class Enviroment:

	def __init__(self, sizeX, sizeY, initPosX, initPosY, dirtRate):
		self.sizeX = sizeX
		self.sizeY = sizeY
		self.initPosX = initPosX
		self.initPosY = initPosY
		self.dirtRate = dirtRate
		self.matrix = self.fillMatrix(dirtRate)
		self.currentPosX = initPosX
		self.currentPosY = initPosY
	
	def fillMatrix(self, dirtRate):
		matrix = [[0 for i in range(self.sizeX)] for j in range(self.sizeY)]
		slots = self.sizeX**2
		dirtySlots = slots * dirtRate

		# Fills the matrix with random dirty slots with as many dirty slot
		# as the dirt rate indicates (totalSlots*dirtRate)
		# this is less precise when we have small enviroments, for example:
		# 0.8 dirtRate is not possible in 2x2 enviroments since we only have 4 slots.
		while dirtySlots > 0:
			x = randint(0, self.sizeX - 1)
			y = randint(0, self.sizeY - 1)

			if(matrix[y][x] == 0):
				matrix[y][x] = 1
				dirtySlots = dirtySlots - 1

		return matrix

	def isDirty(self):
		return self.matrix[self.currentPosY][self.currentPosX] == 1
	
	def acceptAction(self, action):
		action()

	def getPerformance(self):
		verifyDirtiness(self.matrix)
	
	def printEnviroment(self):
		printMatrix(self.matrix)

	


	