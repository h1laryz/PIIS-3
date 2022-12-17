import chess


def count(board, turn):
    if turn == 1:
        chosen = board.occupied_co[chess.WHITE]
    else:
        chosen = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(chosen & board.pawns) + chess.popcount(chosen & board.knights) +
        chess.popcount(chosen & board.bishops) + chess.popcount(chosen & board.rooks) +
        chess.popcount(chosen & board.queens)
    )


def materialBalance(board):
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
        3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
        3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
        5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
        9 * (chess.popcount(white & board.queens) -
             chess.popcount(black & board.queens))
    )


def eval(board, turn):
    countWhite = count(board, 1)
    countBlack = count(board, -1)
    material_balance = materialBalance(board)
    return material_balance * (countWhite - countBlack) * turn
