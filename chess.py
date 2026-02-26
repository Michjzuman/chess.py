import random
import os

class Player:
    def __init__(self, id: int, name: str, controller):
        self.id = id
        self.name = name
        self.controller = controller
        self.color = [
            "white", "black"
        ][self.id]

class Piece:
    def __init__(self, player_id: int):
        self.player_id = player_id
        self.symbol: str
        self.code: str
        self.x: int
        self.y: int

class Pawn(Piece):
    def __init__(self, player_id: int):
        super().__init__(player_id)

class Board:
    def __init__(self):
        self.lines = [
            
        ] + [
            [None for _ in range(8)]
            for _ in range(4)
        ]
    
    def draw(self, *, coorditates = True):
        print(
            f" \033[90m{' '.join([f' {"abcdefgh"[i]} ' for i in range(8)])}\033[0m" +
            f"\n╔{'╤'.join(['═══'] * 8)}╗" +
            f"\n╟{'┼'.join(['───'] * 8)}╢".join([
                f"""\n║{'│'.join([
                    f''' {
                        "_"
                    } ''' for x, field in enumerate(line)
                ])}║ \033[90m{8 - y}\033[0m"""
                for y, line in enumerate(self.lines)
            ]) +
            f"\n╚{'╧'.join(['═══'] * 8)}╝" +
            f"\n \033[90m{' '.join([f' {"abcdefgh"[i]} ' for i in range(8)])}\033[0m"
        )

class Game:
    def __init__(self):
        self.history = []
        self.board = Board()

def play():
    game = Game()
    os.system("clear; clear")
    game.board.draw(coorditates = True)

if __name__ == "__main__":
    play()