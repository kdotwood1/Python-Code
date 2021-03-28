#!/usr/bin/python3

#---------------------------------------------------------------------------
# Functions
def getNumber():
    while True:        
        try:
            n = int(input("Enter 0, 1 or 2: "))
        except ValueError:
            n = -1
        if n >= 0 and n <= 2: 
            break      #this is a valid number, leave the loop
            
        print("Please Enter 0, 1, or 2")  #print message and try again
    return n

def drawBoard():
    #print the board
    for row in range(0, 3):
        for col in range(0, 3):
            print("%1s" % board[row][col], sep="", end="")
            if (col < 2): 
                print("|", sep="", end="")
        print("")
        if ( row < 2 ):
            print("-+-+-")

#---------------------------------------------------------------------------
# Mainline
board = [ [ "", "", "" ], [ "", "", "" ], [ "", "", "" ] ]

#Select who starts
while True:
    piece = input("Who starts, X or O?: ").upper()
    if piece == "X" or piece == "O":
        break
    print("Please enter O or X")

while (True):
    drawBoard()

    print("\n", piece, "'s turn", sep="")
    while True:
        print("Row: ", end=""); row = getNumber()
        print("Col: ", end=""); col = getNumber()

        #If the selected position is free, we have a valid move
        if board[row][col] == "":
            break;

        print("That position is ocupied by", board[row][col])
    
    #play the seltected move and change the turn
    board[row][col] = piece
    piece = "O" if piece == "X" else "X"
