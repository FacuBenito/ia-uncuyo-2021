from environment import *
from agent import *

env = Environment(randint(0,19), randint(0,19), randint(0,19), randint(0,19))
env.printEnvironment()

agent = Agent(env)
solution = agent.breadthFirstSearch()

if(solution != False):
	agent.goToGoal(solution)
	agent.env.printEnvironment()