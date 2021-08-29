from node import Node
from random import randint

class Environment:

	def __init__(self, initPosY, initPosX, goalPosY, goalPosX):
		self.matrix = self.fillMatrix()
		self.initPosX = initPosX
		self.initPosY = initPosY
		self.goalPosX = goalPosX
		self.goalPosY = goalPosY
		self.matrix[initPosY][initPosX] = Node('start', 0, initPosY, initPosX)
		self.matrix[goalPosY][goalPosX] = Node('goal', 1, goalPosY, goalPosX)
		self.currentPosX = initPosX
		self.currentPosY = initPosY

	def fillMatrix(self):
		matrix = [[Node('normal', 1, j, i) for i in range(100)] for j in range(100)]
		obstacleCount = 2500

		while obstacleCount > 0:
			y = randint(0,99)
			x = randint(0,99)

			if(
				matrix[y][x].nodeType != 'start' and 
				matrix[y][x].nodeType != 'goal' and 
				matrix[y][x].nodeType != 'obstacle'
			):
				matrix[y][x] = Node('obstacle', 1, y, x)
				obstacleCount = obstacleCount - 1

		return matrix

	def printEnvironment(self):
		matrix = self.matrix

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				print(matrix[i][j].icon, end='')
			print('')
		
	
