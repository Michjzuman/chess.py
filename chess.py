import random
import os

def render(board, game):
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
    print(f"         {WHITE} • {WHITE}python chess{WHITE} •{RESET}")
    print()
    print(f"{WHITE}  ╔{'╤'.join(['═══'] * 8)}╗{RESET_TO_WHITE}")
    moves_line = 0
    for y, line in enumerate(reversed(board)):
        render_lines = [
            f"{GRAY}{list(reversed(list('abcdefgh')))[y]}{RESET_TO_WHITE} ║",
            f"{WHITE}  {'╚' if y == len(board) - 1 else '╟'}{RESET_TO_WHITE}"
        ]
        for x, square in enumerate(line):
            square_white = x % 2 == (0 if y % 2 == 0 else 1)
            piece_white = square != square.lower()
            bg_color = '100' if square_white else '40'
            only_bg_color = f"\033[{bg_color};37m"
            color = f"\033[{bg_color}{';37' if piece_white else ';33'}m"
            render_lines[0] += f"{color} {square.upper()}{RESET_TO_WHITE}{only_bg_color} {'║' if x == len(line) - 1 else'│'}{RESET_TO_WHITE}"
            render_lines[1] += f"{only_bg_color}{('═' if y == len(board) - 1 else'─') * 3}{('╝' if x == len(line) - 1 else '╧') if y == len(board) - 1 else ('╢' if x == len(line) - 1 else'┼')}{RESET_TO_WHITE}"
        move_notation_1 = f"{' ' * 3} {'' if len(game) <= moves_line else game[moves_line]}"
        move_notation_2 = f"{'' if len(game) <= (moves_line + 1) else (f' {GRAY}-{WHITE} ' + game[moves_line + 1])}"
        render_lines[0] += move_notation_1 + move_notation_2
        for render_line in render_lines:
            print(render_line)
        moves_line += 2
    print(f"{GRAY}    {'   '.join([str(i + 1) for i in range(8)])}{RESET}")

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
    game = [
        "e4", "e5",
        "Nf3", "Nf6",
        "Nxe5", "Nxe4",
        "Qc6", "f1",
        "Qxg6#"
    ]
    board = imagine_board(game)
    
    render(board, game)

if __name__ == "__main__":
    main()
