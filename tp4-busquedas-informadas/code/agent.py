from node import icons
from math import sqrt

class Agent:
	def __init__(self, environment):
		self.env = environment
		self.explored = [] # For DFS
		self.stateCount = 0

	def up(self):
		env = self.env
		env.currentPosY = env.currentPosY - 1

	def down(self):
		env = self.env
		env.currentPosY = env.currentPosY + 1

	def left(self):
		env = self.env
		env.currentPosX = env.currentPosX - 1

	def right(self):
		env = self.env
		env.currentPosX = env.currentPosX + 1

	def checkUp(self, state):
		env = self.env
		return env.matrix[state[0] - 1][state[1]]

	def checkDown(self, state):
		env = self.env
		return env.matrix[state[0] + 1][state[1]]

	def checkLeft(self, state):
		env = self.env
		return env.matrix[state[0]][state[1] - 1]

	def checkRight(self, state):
		env = self.env
		return env.matrix[state[0]][state[1] + 1]

	def checkCostToGoal(self, currentState):
		goalY = self.env.goalPosY
		goalX = self.env.goalPosX
		posY = currentState[0]
		posX = currentState[1]

		deltaY = abs(posY - goalY)
		deltaX = abs(posX - goalX)

		return (deltaY + deltaX)

	def getActions(self, currentState, frontier, explored):
		matrix = self.env.matrix
		posY = currentState[0]
		posX = currentState[1]
		actions = []

		if(
			posX < len(matrix[0]) - 1 and 
			matrix[posY][posX + 1].nodeType != 'obstacle' and 
			matrix[posY][posX + 1].state not in explored and 
			matrix[posY][posX + 1].state not in frontier
		):
			matrix[posY][posX + 1].parent = matrix[posY][posX]
			matrix[posY][posX + 1].cost = matrix[posY][posX].cost + self.checkCostToGoal(currentState)
			actions.append('checkRight')
	
		if(
			posY < len(matrix) - 1 and 
			matrix[posY + 1][posX].nodeType != 'obstacle' and 
			matrix[posY + 1][posX].state not in explored and 
			matrix[posY + 1][posX].state not in frontier
		):
			matrix[posY + 1][posX].parent = matrix[posY][posX]
			matrix[posY + 1][posX].cost = matrix[posY][posX].cost + self.checkCostToGoal(currentState)
			actions.append('checkDown')
		
		if(
			posX > 0 and 
			matrix[posY][posX - 1].nodeType != 'obstacle' and 
			matrix[posY][posX - 1].state not in explored and 
			matrix[posY][posX - 1].state not in frontier
		):
			matrix[posY][posX - 1].parent = matrix[posY][posX]
			matrix[posY][posX - 1].cost = matrix[posY][posX].cost + self.checkCostToGoal(currentState)
			actions.append('checkLeft')
		
		
		if(
			posY > 0 and 
			matrix[posY - 1][posX].nodeType != 'obstacle' and 
			matrix[posY - 1][posX].state not in explored and 
			matrix[posY - 1][posX].state not in frontier
		):
			matrix[posY - 1][posX].parent = matrix[posY][posX]
			matrix[posY - 1][posX].cost = matrix[posY][posX].cost + self.checkCostToGoal(currentState)
			actions.append('checkUp')

		return actions

	def goToGoal(self, solution):
		matrix = self.env.matrix
		currentNode = solution
		states = []

		while currentNode != None:
			states.append(currentNode.state)
			currentNode = currentNode.parent
			
		for i in range(len(states)):
			state = states[i]
			if(matrix[state[0]][state[1]].nodeType == 'normal'):
				matrix[state[0]][state[1]].icon = getattr(icons, 'path')
		
		self.env.printEnvironment

		return len(states)

	def getSortKey(self, state):
		matrix = self.env.matrix
		return matrix[state[0]][state[1]].cost

	def AStarSearch(self):
		env = self.env
		matrix = env.matrix
		startNode = matrix[env.initPosY][env.initPosX]

		frontier = [startNode.state]
		explored = []

		while True:
			if(frontier == []):
				return False
			
			currentNode = frontier.pop(0)
			self.stateCount += 1
			
			posY = currentNode[0]
			posX = currentNode[1]

			if(currentNode != (env.initPosY, env.initPosX)):
				matrix[posY][posX].icon = getattr(icons, 'explored')

			if(posY == env.goalPosY and posX == env.goalPosX):
				return matrix[posY][posX]

			explored.append(currentNode)
			actions = self.getActions(currentNode, frontier, explored)

			for action in actions:
				callback = getattr(self, action)
				nextNode = callback(currentNode)

				if(nextNode.state[0] == env.goalPosY and nextNode.state[1] == env.goalPosX):
					return matrix[nextNode.state[0]][nextNode.state[1]]

				frontier.append(nextNode.state)
				frontier.sort(key = self.getSortKey)
	