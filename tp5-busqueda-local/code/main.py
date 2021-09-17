from board import *
from genetic import *
import time
import statistics

# hillClimbingResults = []
# hillClimbingStates = []
# hillClimbingTimes = []

# for i in range(30):
# 	board1 = Board(8)

# 	start = time.time()
# 	h = board1.hillClimbing()
# 	end = time.time() - start
# 	stateCount = board1.stateCount

# 	if(h == 0):
# 		hillClimbingResults.append(h)
# 	hillClimbingStates.append(stateCount)
# 	hillClimbingTimes.append(end)

# hillClimbingSuccessfulPCT = (30 / len(hillClimbingResults)) *100

# hillClimbingTimeSD = statistics.stdev(hillClimbingTimes)
# hillClimbingTimeMean = statistics.mean(hillClimbingTimes)
# hillClimbingStatesSD


# simulatedAnnealingResults = []
# simulatedAnnealingStates = []
# simulatedAnnealingTimes = []

# for i in range(30):
# 	board2 = Board(10)

# 	start = time.time()
# 	h = board2.hillClimbing()
# 	end = time.time() - start
# 	stateCount = board1.stateCount

# 	simulatedAnnealingResults.append(h)
# 	simulatedAnnealingStates.append(stateCount)
# 	simulatedAnnealingTimes.append(end)

gen = Genetic(8)
solution = gen.getSolution()
solution.print_board()
print(solution.calculateResult())