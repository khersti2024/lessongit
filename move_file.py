def move(board, mark, position):
  new_board = board[:position] + mark + board[position+1:]
  return new_board


