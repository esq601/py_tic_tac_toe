import numpy as np
import randbot as rb
import random

class tic_tac_toe():

    def __init__(self):
        self.board = np.zeros((3,3),dtype=np.int8)
        self.player = 1    
        
    def numplayer(self,nplay=2):
        numplayer = nplay
        return numplayer

    def show_board(self):
        print(self.board)

    def action(self,nplay):

        numplayer = nplay

        if numplayer <= 1:
            print(f"Player {self.player}'s turn")

        while True:
            try:
                if (
                    numplayer >= 1 
                    and self.player == -1):
                    
                    choice = rb.choice()

                elif (
                    numplayer == 2
                    and self.player == 1):
                    choice = rb.choice()

                else:
                    row = input("Enter row number")
                    col = input("Enter column number")
                    rownum = int(row)-1
                    colnum = int(col)-1
                    choice = [rownum,colnum]

                if (
                    self.board[choice[0],choice[1]] == 0
                    and 0 <= choice[0]
                    and 0 <= choice[1]
                    and choice[0] <= 2
                    and choice[1] <= 2
                ):
                    break
            except:
                pass
            if numplayer <= 1:
                print("Invalid Input (Must be 1,2,3 and a 0 on board).") 
        return choice

    def turn(self, nplay):

        numplayer = nplay

        choice = self.action(nplay = numplayer)

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

        victor = []

        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            print(f"Player {self.player} Won!")
            game = True
            victor = self.player

        elif abs(sum(np.diagonal(self.board))) == 3:
            print(f"Player {self.player} Won!")
            game = True
            victor = self.player

        elif len(self.legal_actions()) == 0:
            print("Tie game")
            game = True
            victor = 0

        else:
            for i in range(3):

                if abs(np.sum(self.board[i:i+1])) == 3:
                    print(f"Player {self.player} Won!")
                    game = True
                    victor = self.player
                    
                if abs(np.sum(self.board[:,i:i+1])) == 3:
                    print(f"Player {self.player} Won!")
                    game = True
                    victor = self.player
               
        if game == True:

            return True, victor
        else:
            return False, victor
 

    def loop(self, nplay):
        
        numplayer = nplay

        victory,winner = self.victory_conditions()

        while victory == False:

            if numplayer <= 1:
                self.show_board()

            self.turn(nplay = numplayer)
            victory, winner = self.victory_conditions()
            self.player = -1 * self.player

        if numplayer <= 1:
            self.show_board()

        return winner


if __name__ == "__main__":
    game = tic_tac_toe()
    #numplayer = int(input("Input bot players"))

    numplay = int(input("Input bot players"))
    
    game.loop(nplay = numplay)