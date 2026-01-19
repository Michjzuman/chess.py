import random
import os

def render(board):
    os.system("clear")
    separator = f"+{'+'.join(["---"] * 8)}+\n"
    line = f"|{'|'.join(["   "] * 8)}|\n"
    print(line.join([separator] * 8))
    
    for y, line in enumerate(board):
        print("".join([
            f"\033[{100 if x % 2 == (0 if y % 2 == 0 else 1) else 40}m {square} \033[0m"
        for x, square in enumerate(line)]))

def imagine_board(game):
    def get_start_board():
        strong_row = "RNBQKBNR"
        pawn_row = "P" * 8
        empty_row = [" "] * 8
        return [
            list(strong_row),
            list(pawn_row),
            empty_row, empty_row,
            empty_row, empty_row,
            list(pawn_row.lower()),
            list(strong_row.lower())
        ]
    
    start_board = get_start_board()
    
    return start_board

def main():
    game = []
    board = imagine_board(game)
    render(board)
    print("Hello World!")

if __name__ == "__main__":
    main()