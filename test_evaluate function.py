import evaluate_file as ef
import move_file as mf

#evaluate function testing
x_wins = ef.evaluate("--xoox--xxo-o-oxxx--o--o-----")
assert x_wins == "x" ## if x won


o_wins = ef.evaluate("--xoox--xxo-ooox-x-----------")
assert o_wins == "o" ## if o won


nobody_wins = ef. evaluate("oxooxooxxoxooxo")
assert nobody_wins == "!" #if nobody won


#move function testing
board = "----------"
new_board = mf.move(board, position = 5,mark = "x")
assert len(board) == len(new_board)
assert board != new_board






