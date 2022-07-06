import copy
import itertools
import random
import tkinter.messagebox
from tkinter import *

board_size = 10  # the size of the playing field
number_for_win = 5  # count for win
board = [[0] * board_size for item in range(board_size)]  # creating a playing field

game_run = True
field = []
cross_count = 0

root = Tk()
root.title('Крестики-нолики')
root.geometry("620x715")
root.resizable(False, False)


def render_board():
    for row in range(board_size):
        line = []
        for col in range(board_size):
            button = Button(root, text=' ', width=4, height=2,
                            font=('Verdana', 14, 'bold'),
                            background='lavender',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_button = Button(root, text='Новая игра', command=new_game, font=('Courier', 14, 'bold'))
    new_button.grid(row=board_size + 1, column=0, columnspan=board_size, sticky='nsew')


def new_game():
    global game_run, cross_count, board
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    game_run = True
    cross_count = 0
    board = [[0] * board_size for item in range(board_size)]


def click(row, col):
    global game_run, cross_count
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        board[row][col] = -1
        cross_count += 1
        win = wins(board, -1)
        if win:
            tkinter.messagebox.showinfo("Info", "Вы проиграли!")
            game_run = False

        if game_run and cross_count < 50:
            computer_move()
            win = wins(board, 1)
            if win:
                tkinter.messagebox.showinfo("Info", "Вы победили!")
                game_run = False


def wins(state, player):
    def get_rows(grid):
        return [[c for c in r] for r in grid]

    def get_cols(grid):
        return zip(*grid)

    def get_backward_diagonals(grid):
        b = [None] * (len(grid) - 1)
        grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
        return [[c for c in r if c is not None] for r in get_cols(grid)]

    def get_forward_diagonals(grid):
        b = [None] * (len(grid) - 1)
        grid = [b[:i] + r + b[i:] for i, r in enumerate(get_rows(grid))]
        return [[c for c in r if c is not None] for r in get_cols(grid)]

    def get_vertical_lines(grid):
        lst = []
        for i in range(len(grid)):
            tmp_lst = []
            for j in range(len(grid)):
                tmp_lst.append(grid[j][i])
            lst.append(tmp_lst)
        return lst

    def get_horizontal_lines(grid):
        lst = []
        for i in range(len(grid)):
            lst.append(grid[i])
        return lst

    backward = get_backward_diagonals(state)
    forward = get_forward_diagonals(state)
    horizontal = get_horizontal_lines(state)
    vertical = get_vertical_lines(state)

    def win(lst: list):
        it = False
        for i in lst:
            if len(i) > 4:
                for item, group in itertools.groupby(i):
                    l = len(list(group))
                    if item == player and l >= 5 or item == player and l >= 5:
                        it = True
        return it

    if win(backward) or win(forward) or win(horizontal) or win(vertical) is True:
        return True
    else:
        return False


def move_0(row, col):
    if field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'O'
        board[row][col] = 1
        return True


def computer_move():
    # logic AI computer
    count = 0
    while True:
        global board
        can_loss = True
        tmp_board = copy.deepcopy(board)
        col = random.randint(0, 9)
        row = random.randint(0, 9)
        if tmp_board[row][col] == 0:
            tmp_board[row][col] = 1
            can_loss = wins(tmp_board, 1)
            tmp_board = []
        if can_loss is False:
            if move_0(row, col):
                break
        count += 1
        if count > 300:
            if move_0(row, col):
                break


render_board()
root.mainloop()
