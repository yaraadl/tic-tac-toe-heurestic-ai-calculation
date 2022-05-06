#YARA ADEL HASSAN MOHAMED 19100683 
#X/O PROJECT 1 AI
import random


class TicTacToe:

    # fun to calculate the heurestic
    def heurestic(self,n,player):
        ho=0
        hx=0
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == "x" or "-" :
                    hx+=1
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == "o" or "-" :
                    ho+=1  
        h=ho-hx 
        print(f"h=ho-hx,{h}={ho}-{hx}")        
        print(f"Heurestic = {h}")
        return h 

    #fun to check if place exists or out of bound
    def Free(self,row,col):
        if row>2 or row<0 or col>2 or col<0:
            print(f"this position is out of bored")
            print(f"__________________________________________________")
            return False
        if self.board[row][col] == "-":
            return True
        else:
            print(f"this position is not free")
            print(f"__________________________________________________")
            return False


    
        
    
# fun to calculate the heurestic
    def newheurestic(self,n,player):
        ho=0
        hx=0
        for i in range(n):
            if self.board[i][0] != "o"   and self. board[i][1] != "o"   and self. board[i][2] != "o"  :
                    hx+=1
            if self.board[i][0] != "x"   and self. board[i][1] != "x"   and self. board[i][2] != "x"  :
                    ho+=1    
            if self.board[0][i] != "o"   and self. board[1][i] != "o"   and self. board[2][i] != "o"  :
                    hx+=1
            if self.board[0][i] != "x"   and self. board[1][i] != "x"   and self. board[2][i] != "x"  :
                    ho+=1

        if self.board[0][0] != "o"   and self. board[1][1] != "o"   and self. board[2][2] != "o"  :
            hx+=1        
        if self.board[0][2] != "o"   and self. board[1][1] != "o"   and self. board[2][0] != "o"  :
            hx+=1
        if self.board[0][0] != "x"   and self. board[1][1] != "x"   and self. board[2][2] != "x"  :    
            ho+=1
        if self.board[0][2] != "x"   and self. board[1][1] != "x"   and self. board[2][0] != "x"  :
            ho+=1

        h=ho-hx 
        print(f"h=ho-hx,{h}={ho}-{hx}")          
        print(f"Heurestic = {h}")
        return h
                   

    #self is an object from class tictactoe
    def __init__(self):
        self.board = []

    def create_board(self):#creating empty bored
        for i in range(3): #bored is  3*3
            row = []
            for j in range(3): #bored is  3*3
                row.append('-') # for each empty place place by "-"
            self.board.append(row)

    def first_player(self):# to choose who will start the game randomly
        return random.randint(0, 1) 
    

    def fixed_position(self, row, col, player):
        
        
    
        while (self.Free(row,col)==False):
            row, col = list(
            map(int, input("Enter row and column numbers : ").split()))
            row=row-1
            col=col-1
        print()
            
                
        self.board[row][col] = player
        

    def win(self, player):
        win = None

        n = len(self.board)####

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


    def full(self):## if we found "-" which represents empty places so then bored is not empty
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_turn(self, player):# avoidding same player to play more than one turn
        return 'x' if player == 'o' else 'o'

    def show_board(self): #printing bored
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):#starting game
        self.create_board() #creating bored

        player = 'x' if self.first_player() == 1 else 'o'
        while True:
            
            n = len(self.board)
            self.newheurestic(n,player)
            print(f"Player {player} turn")

            self.show_board()

            print(f"__________________________________________________")
            # taking user input
            ####################################################################################
            row, col = list(
                map(int, input("Enter row and column numbers: ").split()))
            print()
            ###################################################################################

            # fixing the spot
            self.fixed_position(row - 1, col - 1, player)# as any array starts from zero

            # checking whether current player is won or not
            if self.win(player):

                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not #t3adol 
            if self.full():# bored is full without flag of win being assigned to true
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# run game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()