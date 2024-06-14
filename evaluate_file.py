def evaluate(board):
  if "xxx" in board:
    return "x"
  elif "ooo" in board:
    return "o"
  elif "-" not in board:
    return "!"
  else:
    return "-"