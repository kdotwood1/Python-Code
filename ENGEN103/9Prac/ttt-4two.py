#!/usr/bin/python3

board = [ [ "", "", "" ], [ "", "", "" ], [ "", "", "" ] ]

def getNumber():
	while True:
		try:
			n = int(input('Enter 0, 1, 2:'))
		except ValueError:
			n = -1
		if n>=0 and n <=2:
			break
		print('Please enter 0, 1, 2')
	return n

#Select who starts
while True:
    piece = input("Who starts, X or O?: ").upper()
    if piece == "X" or piece == "O":
        break
    print("Please enter O or X")

while True:
    #print the board
    for row in range(0, 3):
        for col in range(0, 3):
            print("%1s" % board[row][col], sep="", end="")
            if (col < 2): 
                print("|", sep="", end="")
        print("")
        if ( row < 2 ):
            print("-+-+-")

                
    print("\n", piece, "'s turn", sep="")

    #get the position for the next move
    while True:
        #get value for the row from the user, checking for valid input
        print('Row:', end=''); row = getNumber()
        print('Col:', end=''); col = getNumber()
        
        #If the selected position is free, we have a valid move
        if board[row][col] == "":
            break

        print("That position is ocupied by", board[row][col])
    
    #play the seltected move and change the turn
    board[row][col] = piece
    piece = "O" if piece == "X" else "X"
