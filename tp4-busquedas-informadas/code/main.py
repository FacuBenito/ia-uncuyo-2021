from agent import *
from environment import *
import statistics


AStar_States = []

for i in range(30):
	print(i)
	env = Environment(randint(0,99),randint(0,99),randint(0,99),randint(0,99))
	agent = Agent(env)
	solution = agent.AStarSearch()

	if(solution != False):
		agent.goToGoal(solution)
	# env.printEnvironment()

	AStar_States.append(agent.stateCount)

print(AStar_States)
print('Media: ', statistics.mean(AStar_States))
print('Desviacion estandar: ', statistics.stdev(AStar_States), '\n')