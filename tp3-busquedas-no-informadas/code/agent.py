from node import icons
from queue import PriorityQueue
class Agent:
	def __init__(self, environment):
		self.env = environment

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
			matrix[posY][posX + 1].cost = matrix[posY][posX].cost + 1
			actions.append('checkRight')
		
		if(
			posX > 0 and 
			matrix[posY][posX - 1].nodeType != 'obstacle' and 
			matrix[posY][posX - 1].state not in explored and 
			matrix[posY][posX - 1].state not in frontier
		):
			matrix[posY][posX - 1].parent = matrix[posY][posX]
			matrix[posY][posX - 1].cost = matrix[posY][posX].cost + 1
			actions.append('checkLeft')
		
		if(
			posY < len(matrix) - 1 and 
			matrix[posY + 1][posX].nodeType != 'obstacle' and 
			matrix[posY + 1][posX].state not in explored and 
			matrix[posY + 1][posX].state not in frontier
		):
			matrix[posY + 1][posX].parent = matrix[posY][posX]
			matrix[posY + 1][posX].cost = matrix[posY][posX].cost + 1
			actions.append('checkDown')
		
		if(
			posY > 0 and 
			matrix[posY - 1][posX].nodeType != 'obstacle' and 
			matrix[posY - 1][posX].state not in explored and 
			matrix[posY - 1][posX].state not in frontier
		):
			matrix[posY - 1][posX].parent = matrix[posY][posX]
			matrix[posY - 1][posX].cost = matrix[posY][posX].cost + 1
			actions.append('checkUp')

		return actions

	def goToGoal(self, solution):
		matrix = self.env.matrix
		currentNode = solution
		states = []

		if(type(solution) == list):
			states = solution
		else:
			while currentNode != None:
				states.append(currentNode.state)
				currentNode = currentNode.parent

		print(states)
			
		for i in range(len(states)):
			state = states[i]
			if(matrix[state[0]][state[1]].nodeType == 'normal'):
				matrix[state[0]][state[1]].icon = getattr(icons, 'path')
		
		self.env.printEnvironment

		return len(states)

	def getSortKey(self, state):
		matrix = self.env.matrix
		return matrix[state[0]][state[1]].cost

	def breadthFirstSearch(self):
		env = self.env
		matrix = env.matrix
		startNode = matrix[env.initPosY][env.initPosX]

		if(startNode.state == (env.goalPosY, env.goalPosX)):
			return matrix[startNode.state[0]][startNode.state[1]]
		
		frontier = [startNode.state]
		explored = []

		while True:
			if(frontier == []):
				return False

			currentNode = frontier.pop(0)
			explored.append(currentNode)

			actions = self.getActions(currentNode, frontier, explored)

			for i in range(len(actions)):
				action = getattr(self, actions[i])
				nextNode = action(currentNode)

				if(nextNode.state[0] == env.goalPosY and nextNode.state[1] == env.goalPosX):
					return matrix[nextNode.state[0]][nextNode.state[1]]

				frontier.append(nextNode.state)
			
	def uniformCostSearch(self):
		env = self.env
		matrix = env.matrix
		startNode = matrix[env.initPosY][env.initPosX]

		frontier = [startNode.state]
		explored = []

		while True:
			if(frontier == []):
				return False
			
			currentNode = frontier.pop(0)
			posY = currentNode[0]
			posX = currentNode[1]

			if(posY == env.goalPosY and posX == env.goalPosX):
				print('Hola')
				return matrix[posY][posX]

			explored.append(currentNode)
			actions = self.getActions(currentNode, frontier, explored)

			for action in actions:
				callback = getattr(self, action)
				nextNode = callback(currentNode)

				if(nextNode.state[0] == env.goalPosY and nextNode.state[1] == env.goalPosX):
					print('Chau')
					return matrix[nextNode.state[0]][nextNode.state[1]]

				frontier.append(nextNode.state)
				frontier.sort(key = self.getSortKey)

	
	def getActionsDLS(self, currentNode, explored):
		matrix = self.env.matrix
		posY = currentNode.state[0]
		posX = currentNode.state[1]

		actions = []

		if(
			posX < len(matrix[0]) - 1 and 
			matrix[posY][posX + 1].nodeType != 'obstacle' and 
			matrix[posY][posX + 1].state not in explored
		):
			actions.append('checkRight')
		
		if(
			posX > 0 and 
			matrix[posY][posX - 1].nodeType != 'obstacle' and 
			matrix[posY][posX - 1].state not in explored
		):
			actions.append('checkLeft')
		
		if(
			posY < len(matrix) - 1 and 
			matrix[posY + 1][posX].nodeType != 'obstacle' and 
			matrix[posY + 1][posX].state not in explored
		):
			actions.append('checkDown')
		
		if(
			posY > 0 and 
			matrix[posY - 1][posX].nodeType != 'obstacle' and 
			matrix[posY - 1][posX].state not in explored
		):
			actions.append('checkUp')

		return actions

	def depthLimitedSearch(self):
		matrix = self.env.matrix
		initY = self.env.initPosY
		initX = self.env.initPosX

		print(initY, initX)
		print(self.env.goalPosY, self.env.goalPosX)

		explored = []

		return self.DLS_Recursive(matrix[initY][initX], explored, 200)

	def DLS_Recursive(self, currentNode, explored, limit):
		env = self.env

		if(currentNode.state == (env.goalPosY, env.goalPosX)):
			return explored
		elif (limit == 0):
			return False
		
		explored.append(currentNode.state)

		actions = self.getActionsDLS(currentNode, explored)

		for action in actions:
			callback = getattr(self, action)
			nextNode = callback(currentNode.state)

			if(nextNode.state == (env.goalPosY, env.goalPosX)):
				return explored

			result = self.DLS_Recursive(nextNode, explored, limit - 1)

			if(result != False):
				return result
			return False