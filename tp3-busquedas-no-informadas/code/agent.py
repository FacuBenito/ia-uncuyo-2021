from node import icons

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
			actions.append('checkRight')
		
		if(
			posX > 0 and 
			matrix[posY][posX - 1].nodeType != 'obstacle' and 
			matrix[posY][posX - 1].state not in explored and 
			matrix[posY][posX - 1].state not in frontier
		):
			matrix[posY][posX - 1].parent = matrix[posY][posX]
			actions.append('checkLeft')
		
		if(
			posY < len(matrix) - 1 and 
			matrix[posY + 1][posX].nodeType != 'obstacle' and 
			matrix[posY + 1][posX].state not in explored and 
			matrix[posY + 1][posX].state not in frontier
		):
			matrix[posY + 1][posX].parent = matrix[posY][posX]
			actions.append('checkDown')
		
		if(
			posY > 0 and 
			matrix[posY - 1][posX].nodeType != 'obstacle' and 
			matrix[posY - 1][posX].state not in explored and 
			matrix[posY - 1][posX].state not in frontier
		):
			matrix[posY - 1][posX].parent = matrix[posY][posX]
			actions.append('checkUp')

		return actions

	def goToGoal(self, endNode):
		matrix = self.env.matrix
		currentNode = endNode
		states = []

		while currentNode != None:
			states.append(currentNode.state)
			currentNode = currentNode.parent
			
		for i in range(len(states)):
			state = states[i]
			if(matrix[state[0]][state[1]].nodeType == 'normal'):
				matrix[state[0]][state[1]].icon = getattr(icons, 'path')
		
		self.env.printEnvironment

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
					print('Llegué!')
					return matrix[nextNode.state[0]][nextNode.state[1]]

				frontier.append(nextNode.state)
			