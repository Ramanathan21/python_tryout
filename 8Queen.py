__author__ = 'Ram'
board_size = 8
chess_board = [[0 for x in range(board_size)] for x in range(board_size)]
queen_count = board_size


def capture_horizontally(rank, reverse=False):
    global chess_board
    for index, cell in enumerate(chess_board[rank]):
        if cell != board_size + 1:
            if reverse is False:
                chess_board[rank][index] += 1
            else:
                chess_board[rank][index] -= 1


def capture_vertically(file, reverse=False):
    for rank in chess_board:
        if rank[file] != board_size + 1:
            if reverse is False:
                rank[file] += 1
            else:
                rank[file] -= 1


def capture_diagonal(pos_x, pos_y, reverse=False):
    if pos_x >= pos_y:
        x = pos_x - pos_y
        y = 0
    else:
        y = pos_y - pos_x
        x = 0
    while 0 <= x < board_size and 0 <= y < board_size:
        if chess_board[x][y] != board_size + 1:
            if reverse is False:
                chess_board[x][y] += 1
            else:
                chess_board[x][y] -= 1
        x += 1
        y += 1

    if pos_x + pos_y >= board_size - 1:
        x = pos_x + pos_y - (board_size - 1)
        y = board_size - 1
    else:
        y = pos_x + pos_y
        x = 0
    while 0 <= x < board_size and 0 <= y < board_size:
        if chess_board[x][y] != board_size + 1:
            if reverse is False:
                chess_board[x][y] += 1
            else:
                chess_board[x][y] -= 1
        x += 1
        y -= 1


def display(board):
    for rank in board:
        for cell in rank:
            print(cell, " ", end="")
        print()


def capture(row_index, col_index, reverse=False):
    if reverse is False:
        chess_board[row_index][col_index] = board_size + 1
        capture_horizontally(row_index)
        capture_vertically(col_index)
        capture_diagonal(row_index, col_index)
    else:
        chess_board[row_index][col_index] = 0
        capture_horizontally(row_index, True)
        capture_vertically(col_index, True)
        capture_diagonal(row_index, col_index, True)


def assign_queen():
    queen_assigned = 0
    row_index = 0
    while row_index < board_size - 1:
        ''' check for free cells in row'''
        free_cells = []
        for cells in chess_board[row_index]:
            if cells == 0:
                free_cells.append(cells)
        next_free_row_flag = True
        col_index = 0
        while next_free_row_flag:
            if cell is 0:
                ''' capturing cells'''
                capture(row_index, col_index)

                '''check the next row for free space'''
        row_index += 1


display(chess_board)
assign_queen()
print()
display(chess_board)
