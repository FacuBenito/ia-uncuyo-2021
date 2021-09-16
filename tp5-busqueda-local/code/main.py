from board import *

board = Board(8)

board.printBoard()
print('--------')
print('h', board.hillClimbing())
board.printBoard()

# print('Estados: ', board.stateCount)
# print('Reinas afectadas: ', board.queensAffected)
# board.printBoard()