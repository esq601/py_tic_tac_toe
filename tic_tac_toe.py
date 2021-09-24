import numpy as np

class tic_tac_toe():

    def __init__(self):
        self.board = np.zeros((3,3),dtype=np.int8)
        self.player = 1

    def show_board(self):
        print(self.board)

    def action(self):

        print(f"Player {self.player}'s turn")

        while True:
            try:
                row = input("Enter row number")
                col = input("Enter column number")
                rownum = int(row)-1
                colnum = int(col)-1
                choice = [rownum,colnum]

                if (
                    self.board[choice[0],choice[1]] == 0
                    and 0 <= rownum
                    and 0 <= colnum
                    and rownum <= 2
                    and colnum <= 2
                ):
                    break
            except:
                pass
            print("Invalid Input (Must be 1,2,3 and a 0 on board).") 
        return choice

    def turn(self):
        choice = self.action()

        if self.player == 1:
            choice_val = 1
        else:
            choice_val = -1
        self.board[choice[0],choice[1]] = choice_val

    def legal_actions(self):
        legal = []
        for i in range(9):
            row = i // 3
            col = i % 3
            if self.board[row, col] == 0:
                legal.append(i)
        return legal


    def victory_conditions(self):

        game = False

        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            print(f"Player {self.player} Won!")
            game = True

        elif abs(sum(np.diagonal(self.board))) == 3:
            print(f"Player {self.player} Won!")
            game = True

        elif len(self.legal_actions()) == 0:
            print("Tie game")
            game = True

        else:
            for i in range(3):
                print(i)
                if abs(np.sum(self.board[i:i+1])) == 3:
                    print(f"Player {self.player} Won!")
                    game = True
                    
                if abs(np.sum(self.board[:,i:i+1])) == 3:
                    print(f"Player {self.player} Won!")
                    game = True
               
        if game == True:
            self.show_board()
            return True
        else:
            return False
 

    def loop(self):

        victory = self.victory_conditions()
        print(victory)
        while victory == False:
            self.show_board()
            self.turn()
            victory = self.victory_conditions()
            self.player = -1 * self.player




game = tic_tac_toe()
game.loop()