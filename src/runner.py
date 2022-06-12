from Board import Board
from RandomPlayer import RandomPlayer

players = [RandomPlayer(f"Radom {x}") for x in range(4)]
board = Board(104, 4, 6, players, 10)
board.run()
