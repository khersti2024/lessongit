introduction_start = "Welcome to the game. The player who places three of their own marks next to each other wins. You take the x and the Pc has the o. So enough talking, let's start the game!"
print (introduction_start)

board = '-' *20

while "-" in board:
    marks = input("Enter your mark [x or o]: ")
    position = int(input("Where do you want to go [1-19]: "))

#player move
    if position in range (0,19) and board[position] == "-":
        if marks.lower() == "x" or marks.lower() == "o":
            board = board[:position] + marks + board[position:]
            print (board)
 #check for winner after player's move 
    if "xxx" in board:
         print("Xs has won")
         break
    if "ooo" in board:
        print("Os has won")
        break
    if "-" not in board:
        print("draw, the board is full but nobody has won")
        break
    
    #computer move
    import random
    pc_position = random.randrange(0, 19)
    while board[pc_position] != "-":
        pc_position = random.randrange(0, 19)
    board = board[:pc_position] + 'o' + board[pc_position+1:]
    print(board)        
   
#check for winner after computer's move
    if "xxx" in board:
        print("Xs has won")
        break
    if "ooo" in board:
        print("Os has won")
        break     
    if "-" not in board:
        print("Draw, the board is full but nobody has won")
        break













              
    
            
        



    
