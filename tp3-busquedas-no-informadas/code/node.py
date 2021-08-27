# Anonymous object so that I can easily get each icon
icons = type('',(object,),{
	'goal': u"\u2705",
	'start': u'\u26F2',
	'obstacle': u'\u26D4', 
	'path':   u'\u26AA',
	'normal': u'\u26AB'
	})()

# Frontera: nodos a los que me puedo mover pero no he explorado
# State: nodos a los que me puedo mover

class Node:
	def __init__(self, nodeType, cost, stateY, stateX):
		self.nodeType = nodeType
		self.cost = cost
		self.state = (stateY, stateX)
		self.icon = getattr(icons, nodeType)
		self.parent = None
