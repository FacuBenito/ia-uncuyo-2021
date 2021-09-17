import random
import time
from operator import itemgetter
from slot import *

class Genetic:
	def __init__(self,size):
			self.population = []
			self.size = size
			self.worse = 0

			for i in range(size-1):
					self.worse += (size-1)-i

			for i in range(100):
					b = Board(size)
					self.population.append(b)

	def getSolution(self):

		for i in range(len(self.population)):
				self.population[i].print_board()
				print(self.population[i].calculateResult())
				print()

		self.best = None
		self.bestFit = self.worse
		self.stateCount = None
		self.saveForGraph = []
		for i in range(200):
				self.newPopulation()
				self.getBest(i)

		return self.best

	# def solution(self):
	# 	startTime = time.time()

	# 	self.best = None
	# 	self.bestFit = self.worse
	# 	self.stateCount = None
	# 	self.saveForGraph = []

	# 	for i in range(200):
	# 			self.newPopulation()
	# 			self.getBest(i)

	# 	endTime = time.time() - startTime
	# 	return (self.best.calculateResult(), self.stateCount, endTime, self.saveForGraph)

	def newPopulation(self):
			newPopulation = []

			for i in range(int(len(self.population)/2)):
					parents = self.getParents()
					childs = self.reproduce(parents)
					newPopulation.extend(childs)
					olds = self.keepBestSolutions()
					remaining = self.eliminateWorstSolutions(newPopulation)

			olds.extend(remaining)
			self.population = olds


	def getParents(self):
			element1 = None
			element2 = None
			while (element1 == None):
					random1 = random.randint(0, len(self.population)-1)
					random2 = random.uniform(0, 1)
					fitness = self.worse - self.population[random1].calculateResult()
					probability = fitness / self.worse

					if (random2 <= probability):
							element1 = self.population[random1]

			while (element2 == None):
					random1 = random.randint(0, len(self.population)-1)
					random2 = random.uniform(0, 1)
					fitness = self.worse - self.population[random1].calculateResult()
					probability = fitness / self.worse

					if (random2 <= probability and self.population[random1].queensPos != element1.queensPos):
							element2 = self.population[random1]

			return (element1,element2)

	def reproduce(self, parents):
			cut = random.randint(0, self.size - 1)

			child1 = parents[0].queensPos[:cut] + parents[1].queensPos[cut:]
			child1 = self.mutate(child1)
			b1 = Board(self.size)
			b1.queensPos = child1

			child2 = parents[1].queensPos[:cut] + parents[0].queensPos[cut:]
			child2 = self.mutate(child2)
			b2 = Board(self.size)
			b2.queensPos = child2

			return(b1, b2)

	def keepBestSolutions(self):
			elements = []
			for i in range(len(self.population)):
					elements.append((self.population[i], self.population[i].calculateResult()))

			elements = sorted(elements, key=itemgetter(1))

			result = []
			for e in elements:
					result.append(e[0])

			return result[0:int(len(result)/5)]

	def eliminateWorstSolutions(self,newPopulation):
			elements = []
			for i in range(len(newPopulation)):
					elements.append((newPopulation[i], newPopulation[i].calculateResult()))

			elements = sorted(elements, key=itemgetter(1))

			result = []
			for e in elements:
					result.append(e[0])
			
			result.reverse()

			return result[int(len(result)/5):]

	def mutate(self, child):
			randomNum = random.uniform(0, 1)
			if randomNum < 0.3:
					pos = random.randint(0, self.size - 1)
					num = random.randint(0, self.size - 1)
					child = list(child)
					child[pos] = num
					child = ''.join(map(str, child))
			return child

	def getBest(self,count):
			for i in range(len(self.population)):
					cost = self.population[i].calculateResult()
					if cost < self.bestFit:
							self.bestFit = cost
							self.best = self.population[i]
							self.stateCount = count

					if i == 0:
							self.saveForGraph.append(cost)

class Board:
	def __init__(self, size):
			self.size = size
			self.queensPos = [n for n in range(0, self.size)]
			random.shuffle(self.queensPos)
			self.queensPos = ''.join(map(str, self.queensPos))



	def calculateResult(self):
			h = 0
			mainDiagonal = []
			secondaryDiagonal = []

			for i in range(self.size):
					elem1 = int(self.queensPos[i]) - i
					mainDiagonal.append(elem1)

					elem2 = int(self.queensPos[i]) + i
					secondaryDiagonal.append(elem2)

					for j in range(i+1,self.size,1):
							if self.queensPos[i] == self.queensPos[j]:
									h +=1

			for i in range(self.size):
					for j in range(i + 1, self.size, 1):
							if mainDiagonal[i] == mainDiagonal[j]:
									h += 1
							if secondaryDiagonal[i] == secondaryDiagonal[j]:
									h += 1
			return h


	def print_board(self):
			board = []
			for i in range(self.size):
					board.append([])
					for j in range(self.size):
							newSlot = Slot(self.size**2, u"\u2B1C", i, j)
							board[i].append(newSlot)

			queensNodes = []
			for i in range(self.size):
					board[int(self.queensPos[i])][i].slotType = u"\u2B1B"
					queensNodes.append(board[int(self.queensPos[i])][i])


			a = ""
			for k in range(len(board)):
					for j in range(len(board)):
							a += str(board[k][j].slotType)
					print(a)
					a = ""

