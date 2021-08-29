from environment import *
from agent import *
import statistics

BFS_States = []
DLS_States = []
UC_States = []

for i in range(30):
	print(i)
	env1 = Environment(randint(0,99), randint(0,99), randint(0,99), randint(0,99))
	env2 = Environment(randint(0,99), randint(0,99), randint(0,99), randint(0,99))
	env3 = Environment(randint(0,99), randint(0,99), randint(0,99), randint(0,99))

	agent1 = Agent(env1)
	agent2 = Agent(env2)
	agent3 = Agent(env3)

	solution1 = agent1.breadthFirstSearch()
	solution2 = agent2.uniformCostSearch()
	solution3 = agent3.depthLimitedSearch()

	BFS_States.append(agent1.stateCount)
	UC_States.append(agent2.stateCount)
	DLS_States.append(agent3.stateCount)

print('------BFS---------')
print(BFS_States)
print('Media: ', statistics.mean(BFS_States))
print('Desviacion estandar: ', statistics.stdev(BFS_States), '\n')

print('------UCS---------')
print(UC_States)
print('Media: ', statistics.mean(UC_States))
print('Desviacion estandar: ', statistics.stdev(UC_States), '\n')

print('------DLS---------')
print(DLS_States)
print('Media: ', statistics.mean(DLS_States))
print('Deviacion estandar: ', statistics.stdev(DLS_States))