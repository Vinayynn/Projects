import random

class RockPaperScissors:

    def __init__(self):
        self.userName = input("Enter your name : ")
        # self.computerInput = random.choice(['r', 'p', 's'])
        self.userScore = 0
        self.computerScore = 0
    
    def gameBegins(self):      
        for i in range(1, 6):
            print()
            self.userInput = input("Choose between rock(r), paper(p) and scissor(s) : ").lower()
            self.computerInput = random.choice(['r', 'p', 's'])
            print("The computer`s choice is :", self.computerInput)
            print("-"*50)
            if self.userInput == self.computerInput:
                print("None score a point")
                print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")
                print("-"*50)
            
            else:
                winOrlose = RockPaperScissors.winningCondition(self, self.userInput, self.computerInput)
                print(winOrlose)
                if winOrlose:
                    self.userScore = self.userScore + 1
                    print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")
                    print("-"*50)
                else:
                    self.computerScore = self.computerScore + 1
                    print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")
                    print("-"*50)
        
        if self.userScore > self.computerScore:
            print(f"The winner is {self.userName}")
            print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")
        elif self.userScore == self.computerScore:
            print(f"It`s a tie")
            print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")
        else:
            print(f"The winner is COMPUTER")
            print(f"The scores are, \n{self.userName} --> {self.userScore} and COMPUTER --> {self.computerScore}")


    def winningCondition(self, player1Input, player2Input):
        if (player1Input == 'r' and player2Input == 's') or (player1Input == 'p' and player2Input == 'r') or (player1Input == 's' and player2Input == 'p'):
            return True
        else:
            return False
    


r1 = RockPaperScissors()
r1.gameBegins()
    
