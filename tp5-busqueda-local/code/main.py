from board import *

board = Board(4)

board.printBoard()

count = 0
for i in range(board.size):
	count = count + board.calculateQueensAffected(board.queensList[i])
print(count)