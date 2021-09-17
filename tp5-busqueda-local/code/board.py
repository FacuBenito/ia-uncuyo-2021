from slot import *
from queen import *
import copy
from random import randint

class Board:
	def __init__(self, size):
		self.size = size
		self.stateCount = 0
		self.limit = 1000
		self.queensAffected = 0
		self.queensList = []
		self.matrix = self.initMatrix(self.size)
		self.time = 1

	def initMatrix(self, size):
		matrix = [[Slot(size**2, 'normal', col, row) for row in range(size)] for col in range(size)]
		hardcodedPos = [4,5,6,3,4,5,6,5]

		for i in range(size):
			x = hardcodedPos[i]
			matrix[x][i] = Slot(size**2, 'queen', x, i)
			self.queensList.append(matrix[x][i])
		
		return matrix

	def printBoard(self):
		for i in range(self.size):
			for j in range(self.size):
				if(self.matrix[i][j].slotType == 'normal'):
					# print(u'\u25A2', end=' ')
					print(self.matrix[i][j].bestState, end=' ')
				else:
					print(u'\u2655', end=' ')
			print()

	def queensAffectEachOther(self, queen1, queen2):
		queen1posX = queen1.posX
		queen1posY = queen1.posY
		queen2posX = queen2.posX
		queen2posY = queen2.posY

		if (queen1posX == queen2posX):  # column
				return True
		if (queen1posY == queen2posY):  # row
				return True
		if (abs(queen1posX - queen2posX) == abs(queen1posY - queen2posY)):  # diagonal
				return True
		return False

	def runThroughQueens(self, queens):
		queensAffected = 0

		for i in range(len(queens)):
			for j in range(i+1, len(queens)):
				if(self.queensAffectEachOther(queens[i], queens[j])):
					queensAffected += 1
		
		return queensAffected 

	def calculateQueensAffected(self):
		matrix = self.matrix

		for row in range(len(matrix)):
			for col in range(len(matrix)):
				queens = self.queensList.copy()
				queens[col] = Slot(len(matrix)**2, 'queen', row, col)
				queensAffected = self.runThroughQueens(queens)
				matrix[row][col].bestState = queensAffected

	def hillClimbing(self):
		matrix = self.matrix
		minimum = self.size**2

		while (self.limit > 0 or minimum > 0):
			currentMinimum = self.size**2
			row = 0
			col = 0

			self.calculateQueensAffected()
			
			for i in range(len(matrix)):
				for j in range(len(matrix)):
					if(matrix[i][j].bestState < currentMinimum):
						currentMinimum = matrix[i][j].bestState
						row = i
						col = j
			if(currentMinimum >= minimum):
				break;
			minimum = currentMinimum
			self.queensList[col].slotType = 'normal'
			self.queensList[col] = matrix[row][col]
			matrix[row][col].slotType = 'queen'
			self.stateCount = self.stateCount + 1
			self.limit -= 1
		
		return minimum


	def simulatedAnnealing(self):
		matrix = self.matrix
		minimum = self.size**2

		while (self.limit > 0 or minimum > 0):
			currentMinimum = self.size**2
			row = 0
			col = 0

			self.calculateQueensAffected()
			
			for i in range(len(matrix)):
				for j in range(len(matrix)):
					randCol = randint(0, len(matrix)-1)
					randRow = randint(0, len(matrix)-1)
					if(matrix[randRow][randCol].bestState < currentMinimum):
						currentMinimum = matrix[randRow][randCol].bestState
						row = randRow
						col = randCol
					else:
						probability = 1 / self.time
						randomNumber = randint(1, 100)

						if(randomNumber <= probability):
							currentMinimum = matrix[randRow][randCol].bestState
							row = randRow
							col = randCol
			if(currentMinimum >= minimum):
				break;
			minimum = currentMinimum
			self.queensList[col].slotType = 'normal'
			self.queensList[col] = matrix[row][col]
			matrix[row][col].slotType = 'queen'
			self.stateCount += 1
			self.time += 1
			self.limit -= 1
		
		return minimum