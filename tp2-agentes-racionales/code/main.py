from environment import *
from agent import *
from random import randint

sizeX = 8
sizeY = sizeX
initPosX = randint(0, sizeX-1)
initPosY = randint(0, sizeY-1)

env = Enviroment(sizeX, sizeY, initPosX, initPosY, .8)
env.printEnviroment()
print('Initial dirt rate')
verifyDirtiness(env.matrix)

agent = Agent(env)

while(agent.actions > 0):
	agent.think()

print('-----------------------------------')

agent.env.printEnviroment()
agent.env.getPerformance()
