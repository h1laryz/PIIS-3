from HelperFunctions.EvaluationFunction import eval
import random


def negaMax(board, depth, turn):
    if depth == 0:
        return eval(board, turn), None

    max_core = float("-inf")
    best_move = None
    for move in board.legal_moves:
        score = -(negaMax(board, depth - 1, -turn)[0])
        if score == 0:
            score = random.random()
        if score > max_core:
            max_core = score
            best_move = move
    return max_core, best_move
