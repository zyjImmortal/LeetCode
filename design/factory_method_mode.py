# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午8:54
# @Author  : zhouyajun
from pygments import console

BLACK, WHITE = ('BLACK', 'WHITE')

class AbstractBoard:
    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()

    def populate_board(self):
        raise NotImplementedError

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append('\n')
        return ''.join(squares)

class CheckersBoard(AbstractBoard):
    def __init__(self, rows, columns):
        super().__init__(10, 10)

    def populate_board(self):
        pass
