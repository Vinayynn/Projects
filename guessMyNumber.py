from random import randint

class GuessMyNumber:

    def __init__(self):
        self.noOfAttempts = 5
        self.inputFromUser = 0
        self.systemGeneratedNumber = randint(1, 20)

    def gameBegins(self):
        print("-"*50)
        print("You have {} chances to guess the number".format(self.noOfAttempts))
        print("-"*50)
        
        for i in range(1, self.noOfAttempts + 1):
            
            self.inputFromUser = int(input("Guess a number between 1 and 20 : "))
            print("-"*50)
            
            if self.inputFromUser in range(1, 21):
                if i==5:
                    if self.inputFromUser == self.systemGeneratedNumber:
                        print("Congragulations, you won in {} attempts".format(i))
                        print("-"*50)
                        break
                    else:
                        self.noOfAttempts = self.noOfAttempts - 1
                        print("Sorry! the number was {}, Better luck next time. Try playing the game again".format(self.systemGeneratedNumber))
                    print("-"*50)

                else:
                    if self.inputFromUser == self.systemGeneratedNumber:
                        print("Congragulations, you win in {} attempts".format(i))
                        print("-"*50)
                        break
                    else:
                        print("Sorry! your guess was wrong try again")
                        self.noOfAttempts = self.noOfAttempts - 1
                        print("You have {} more chances to guess the number".format(self.noOfAttempts))
                        if abs(self.systemGeneratedNumber - self.inputFromUser) <=3 :
                            print("But, You are very close to the number")
                        else:
                            print("You are nowhere close to the number")
                        if i==4:
                            print("Its the last attempt, try your best")
                        print("-"*50)

            else:
                print("You fool, Entered number is out of range")
                self.noOfAttempts = self.noOfAttempts - 1
                print("You have {} more chances to guess the number".format(self.noOfAttempts))
                if i==4:
                    print("Its the last attempt, try your best")
                print("-"*50)

g1 = GuessMyNumber()
g1.gameBegins()
