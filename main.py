import chess
from MainFunctions.NegaMaxAlg import negaMax
from MainFunctions.NegaScoutAlg import negaScout
from MainFunctions.PVCalg import PVC

board = chess.Board()
depth = 5

while not board.is_checkmate():

    print("Current game state:\n")
    print(board)
    userMove = input("Enter your move: ")
    board.push_san(userMove)
    #  move = negaMax(board, depth, turn)[1]
    #  move = negaScout(board, depth, turn, float("-inf"), float("inf"))[1]
    move = PVC(board, depth, -1, float("-inf"), float("inf"))[1]

    board.push(move)
