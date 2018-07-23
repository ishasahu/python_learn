class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.tictacboard = []
        for y in range(board_size):
            self.tictacboard.append([(y,x) for x in range(board_size)])
        print(self.tictacboard)
    
    def check_input(self, coordinates):
        return self.tictacboard[coordinates[0]][coordinates[1]] != 'X' and self.board[coordinates[0]][coordinates[1]] != 'O'
    
    def __str__(self):
        for play in self.tictacboard:
            print(play)
    
    def add_player_input_to_board(self, coordinatesList, mark):
        print(coordinatesList[0])
        print(coordinatesList[1])
        print(self.tictacboard)
        self.tictacboard[coordinatesList[0]][coordinatesList[1]] = mark
                   
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:
    def __init__(self, board, players):
        self.board = board
        self.players = players
    
    def is_game_over(self):
        for rowList in self.board.tictacboard:
            if not all(type(i) is str for i in rowList):
                return False
            else:
                return True
                   
    def has_won(self):
        winMatrix=[[(0, 0), (1, 0), (2, 0)],
          [(0, 1), (1, 1), (2, 1)], 
          [(0, 2), (1, 2), (2, 2)],
          [(0, 0), (0, 1), (0, 2)], 
          [(1, 0), (1, 1), (1, 2)],
          [(2, 0), (2, 1), (2, 2)],
          [(0, 0), (1, 1), (2, 2)], 
          [(0, 2), (1, 1), (2, 0)]]
        for winningrowList in winMatrix:
            tictacrow=[self.board.tictacboard[x][y] for x,y in winningrowList]
            if(tictacrow==['X','X','X'] or tictacrow==['O','O','O'] ):
                print('winning row ',winningrowList)
                return True
        return False
                   
    def play(self):
        while not self.is_game_over():            
            for player in self.players:
                coordinates = input("{} Where will you play?: ".format(player.name))
                coordinatesList = [int(c) for c in coordinates.split(',')]
                print(coordinatesList)
                print(player.symbol)
                if self.board.check_input:                       
                       self.board.add_player_input_to_board(coordinatesList, player.symbol)                       
                else:            
                    print("Invalid input, please enter again")
                    break            
        self.has_won()

if __name__ == '__main__':
    print("Starting Tic-Tac-Toe")
    b1 = Board(3)    
    p1 = Player('Player 1', 'X')
    p2 = Player('Player 2', 'O')
    players = [p1,p2]
    g1 = Game(b1, players)
    g1.play()



