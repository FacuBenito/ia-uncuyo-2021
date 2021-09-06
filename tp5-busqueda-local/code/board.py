from slot import *
from queen import *
from random import randint

class Board:
	def __init__(self, size):
		self.size = size
		self.stateCount = 0
		self.limit = 1000
		self.queensAffected = 0
		self.queensList = []
		self.matrix = self.initMatrix(self.size)

	def initMatrix(self, size):
		matrix = [[Slot('E')for row in range(size)] for col in range(size)]

		for i in range(size):
			x = randint(0, size-1)
			queen = Queen(x,i)
			matrix[x][i] = queen
			self.queensList.append(queen)
		
		return matrix

	def printBoard(self):
		for i in range(self.size):
			for j in range(self.size):
				if(type(self.matrix[i][j]) == Slot):
					print(self.matrix[i][j].bestState, end=' ')
				else:
					print('R', end=' ')
			print()

	def getHorizontalQueens(self, posY):
		matrix = self.matrix
		count = 0

		for i in range(self.size):
			if(type(matrix[posY][i]) == Queen):
				count = count + 1
		return count - 1 #Remove the starting queen as it can't affect itself

	def getDiagonalQueens(self, posY, posX):
		matrix = self.matrix
		size = self.size

		upRightCount = 0
		upLeftCount = 0
		downRightCount = 0
		downLeftCount = 0
		#Search up-right
		i = 0
		while posY - i >= 0 and posX + i < size:
			print(posY - i, posX + i)
			if(type(matrix[posY - i][posX + i]) == Queen):
				upRightCount = upRightCount + 1
			i = i + 1

		#Search up-left
		i = 0
		while posY - i >= 0 and posX - i >= 0:
			if(type(matrix[posY - i][posX - i]) == Queen):
				upLeftCount = upLeftCount + 1
			i = i + 1

		#Search down-right
		i = 0
		while posY + i < size and posX + i < size:
			if(type(matrix[posY + i][posX + i]) == Queen):
				downRightCount = downRightCount + 1
			i = i + 1

		#Search down-left
		i = 0
		while posY + i < size and posX - i >= 0:
			if(type(matrix[posY + i][posX - i]) == Queen):
				downLeftCount = downLeftCount + 1
			i = i + 1

		return upRightCount + upLeftCount + downRightCount + downLeftCount - 4

	def calculateQueensAffected(self, queen):

		#No need to calculate for vertical queens since I know there won't be more than one in each column
		horizontalQueens = self.getHorizontalQueens(queen.posY)
		diagonalQueens = self.getDiagonalQueens(queen.posY, queen.posX)

		return diagonalQueens + horizontalQueens
