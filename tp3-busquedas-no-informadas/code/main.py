from environment import *
from agent import *

# env = Environment(randint(0,19), randint(0,19), randint(0,19), randint(0,19))
env = Environment(0, 0, 19, 19)
env.printEnvironment()

agent = Agent(env)
solution = agent.depthLimitedSearch()

if(solution != False):
	print(agent.goToGoal(solution))
agent.env.printEnvironment()

print(agent.stateCount)