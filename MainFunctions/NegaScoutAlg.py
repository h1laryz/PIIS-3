from HelperFunctions.EvaluationFunction import eval
import random


def negaScout(board, depth, turn, a, b):
    if depth == 0:
        return eval(board, turn), 0

    bestMove = 0
    for legalMove in board.legal_moves:
        score = -(negaScout(board, depth - 1, -turn, -b, -a)[0])
        if a < score < b and depth > 1:
            score2 = -(negaScout(board, depth - 1, -turn, -b, -score))[0]
            score = max(score, score2)
        if score == 0:
            score = random.random()
        if score > a:
            a = score
            bestMove = legalMove
        if a >= b:
            return a, bestMove
        b = a + 1
    return a, bestMove
