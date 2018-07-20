def tictactoe():
    tictactoeList=[]
    
    for y in range(3):
        tictactoeList.append([(y,x) for x in range(3)])
    
    while not isGameOver(tictactoeList):
        player1Coordinates= enterInput('player 1','X',tictactoeList)
        if checkIfInputIsValid(tictactoeList,player1Coordinates):
                tictactoeList=enterPlayerCoordinatestoTicTacToe(tictactoeList,player1Coordinates,'X')
                if hasWon(tictactoeList):
                    print('Player 1 Won')
                    break
        player1Coordinates= enterInput('player 2','O',tictactoeList)
        if checkIfInputIsValid(tictactoeList,player1Coordinates):
                tictactoeList=enterPlayerCoordinatestoTicTacToe(tictactoeList,player1Coordinates,'O')
                if hasWon(tictactoeList):
                    print('Player 2 Won')
                    break
    if isGameOver(tictactoeList):
        print('Game is a Tie')
                
def enterInput(player,mark,tictactoeList):
    printTicTacToe(tictactoeList)
    while True:
        playerCoordinates=input('{} ( {} ), where will you play? '.format(player,mark))
        if checkIfInputIsValid(tictactoeList,playerCoordinates):
            break
        else:
            print('Not a valid input. Try again')
    return playerCoordinates
                
def printTicTacToe(tictactoeList):
    for rowList in tictactoeList:
        print(rowList)

def checkIfInputIsValid(tictactoeList,coordinatesToValidate):
    coordinatesList=[int(i) for i in coordinatesToValidate.split(',')]
    return tictactoeList[coordinatesList[0]][coordinatesList[1]]!='X' and tictactoeList[coordinatesList[0]][coordinatesList[1]]!='O'
        
def isGameOver(ticktactoeList):
    for rowList in ticktactoeList:
        if not all( type(i) is str  for i in rowList):
            return False
    return True
     
        
def enterPlayerCoordinatestoTicTacToe(tictactoeList,coordinates,mark):
    coordinatesList=[int(i) for i in coordinates.split(',')]
    coordinateTuple=(coordinatesList[0],coordinatesList[1])
    for rowIdx,rowList in enumerate(tictactoeList):
        for idx,cell in enumerate(rowList):
            if cell==coordinateTuple:
                if(tictactoeList[rowIdx][idx] != 'X' and  tictactoeList[rowIdx][idx] !='O'):
                    tictactoeList[rowIdx][idx]=mark
    return tictactoeList

def hasWon(tictactoeList):
   winMatrix=[[(0, 0), (1, 0), (2, 0)],
     [(0, 1), (1, 1), (2, 1)], 
     [(0, 2), (1, 2), (2, 2)],
     [(0, 0), (0, 1), (0, 2)], 
     [(1, 0), (1, 1), (1, 2)],
     [(2, 0), (2, 1), (2, 2)],
     [(0, 0), (1, 1), (2, 2)], 
     [(0, 2), (1, 1), (2, 0)]]
   for winningrowList in winMatrix:
       tictacrow=[tictactoeList[x][y] for x,y in winningrowList]
       if(tictacrow==['X','X','X'] or tictacrow==['O','O','O'] ):
           print('winning row ',winningrowList)
           return True
   return False