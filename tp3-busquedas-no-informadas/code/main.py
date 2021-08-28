from environment import *
from agent import *

# env = Environment(randint(0,19), randint(0,19), randint(0,19), randint(0,19))
env = Environment(14, 16, 17, 15)
env.printEnvironment()

agent = Agent(env)
solution = agent.depthLimitedSearch()

print('Llegué')
print(solution)

if(solution != False):
	agent.goToGoal(solution)
	agent.env.printEnvironment()