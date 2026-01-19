import random
import os


def render(board):
    RESET = "\033[0m"
    WHITE = "\033[37m"
    RESET_TO_WHITE = f"{RESET}{WHITE}"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    GRAY = "\033[90m"
    os.system("clear")
    os.system("clear")
    print(f"{WHITE}  +{'+'.join(['---'] * 8)}+{RESET_TO_WHITE}")
    for y, line in enumerate(reversed(board)):
        render_lines = [
            f"{WHITE}{list('abcdefgh')[y]}{RESET_TO_WHITE} |",
            f"{WHITE}  +{RESET_TO_WHITE}"
        ]
        
        for x, square in enumerate(line):
            square_white = x % 2 == (0 if y % 2 == 0 else 1)
            piece_white = square != square.lower()
            bg_color = '100' if square_white else '40'
            only_bg_color = f"\033[{bg_color};37m"
            color = f"\033[{bg_color}{';31' if piece_white else ';34'}m"
            render_lines[0] += f"{color} {square}{RESET_TO_WHITE}{only_bg_color} |{RESET_TO_WHITE}"
            render_lines[1] += f"{only_bg_color}---+{RESET_TO_WHITE}"
        
        for render_line in render_lines:
            print(render_line)
    print(f"{WHITE}    {GRAY}{'   '.join([str(i) for i in range(8)])}{RESET}")

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

if __name__ == "__main__":
    main()
