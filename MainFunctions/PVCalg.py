from HelperFunctions.EvaluationFunction import eval
import random


def PVC(board, depth, turn, a, b):
    if depth == 0:
        return eval(board, turn), None

    bestMove = None
    for legalMove in board.legal_moves:
        score = -(PVC(board, depth - 1, -turn, -b, -a)[0])
        if a < score < b:
            score = -(PVC(board, depth - 1, -turn, -b, -score))[0]
        if score == 0:
            score = random.random()
        if score > a:
            a = score
            bestMove = legalMove
        if a >= b:
            return a, bestMove
        b = a + 1
    return a, bestMove
