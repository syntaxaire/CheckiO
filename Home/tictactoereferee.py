"""
 Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X
 and O) who take turns marking the spaces in a 3Ã3 grid. The player who
 succeeds in placing three respective marks in a horizontal, vertical, or
 diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games
results. You are given a result of a game and you must determine if the game
ends in a win or a draw as well as who will be the winner. Make sure to return
"X" if the X-player wins and "O" if the O-player wins. If the game is a draw,
return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are
players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Precondition: There is either one winner or a draw. len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""

def checkio(grid):
    for player in "XO":
        for row in grid: # check horizontals
            if player == row[0] == row[1] == row[2]: return player
        for col in range(3): # check verticals
            if player == grid[0][col] == grid[1][col] == grid[2][col]:
                return player
        # check diagonals
        if player == grid[0][0] == grid[1][1] == grid[2][2]:
            return player
        if player == grid[0][2] == grid[1][1] == grid[2][0]:
            return player
    # no winner
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
