from environment import *
from agent import *
from random import randint

sizeX = 16
sizeY = sizeX
initPosX = randint(0, sizeX-1)
initPosY = randint(0, sizeY-1)

env = Enviroment(sizeX, sizeY, initPosX, initPosY, .8)
env.printEnviroment()
# verifyDirtiness(env.matrix)

agent = Agent(env)
