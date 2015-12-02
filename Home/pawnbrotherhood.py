"""
Almost everyone in the world knows about the ancient game Chess and has at
least a basic understanding of its rules. It has various units with a wide range
of movement patterns allowing for a huge number of possible different game
positions (for example Number of possible chess games at the end of the n-th
plies.) For this mission, we will examine the movements and behavior of chess
pawns.

Chess is a two-player strategy game played on a checkered game board laid out in
eight rows (called ranks and denoted with numbers 1 to 8) and eight columns
(called files and denoted with letters a to h) of squares. Each square of the
chessboard is identified by a unique coordinate pair Ã¢ÂÂ a letter and a number
(ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with
pawns. A pawn may capture an opponent's piece on a square diagonally in front of
it on an adjacent file, by moving to that square. For white pawns the front
squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build
a pawn defense wall. With this strategy, one pawn defends the others. A pawn is
safe if another pawn can capture a unit on that square. We have several white
pawns on the chess board and only white pawns. You should design your code to
find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns. You
should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Precondition: 0 < pawns Ã¢ÂÂ¤ 8

"""
def x(ref):
    assert 'a' <= ref[0] <= 'h', "File '%r' is not in a-h" % ref[0]
    return ord(ref[0]) - 97

def y(ref):
    assert '1' <= ref[1] <= '8', "Rank '%r' is not in 1-8" % ref[1]
    return int(ref[1]) - 1

def safe_pawns(pawns):
    board = [['','','','','','','',''] for i in range(8)]
    numSafe = 0
    for square in pawns: # populate board
        board[x(square)][y(square)] = 'P'
    for square in pawns: # check our list
        if y(square) == 0: # 1-rank, skip
            continue
        if x(square) == 0: # a-file, check to right
            if board[x(square) + 1][y(square) - 1] == 'P':
                numSafe += 1
        elif x(square) == 7: # h-file, check to left
            if board[x(square) - 1][y(square) - 1] == 'P':
                numSafe += 1
        else: # not an edge case, check both directions
            if board[x(square) - 1][y(square) - 1] == 'P' or board[x(square) + 1][y(square) - 1] == 'P':
                numSafe += 1
    return numSafe

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
