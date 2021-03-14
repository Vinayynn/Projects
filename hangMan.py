class Hangman:

    def __init__(self):
        self.wordToBeGuessed = "soujanya"
        self.wordToBeGuessedList = []
        self.userGuessList = ["_"] * ( len(self.wordToBeGuessed))
        self.wrongGuesses = list()

    def startGuessing(self):
        print()
        print(f"The word has {len(self.wordToBeGuessed)} letters")
        print(["_"]* len(self.wordToBeGuessed))
        print("-"*50)
        for i in range (11):
            self.userGuess = input("Guess a letter : ").lower()
            if self.userGuess in self.wordToBeGuessed:
                print("You guessed it right and the position of it is as below")
                print()
                self.indexOfWordToBeGuessed = self.wordToBeGuessed.index(self.userGuess)
                if self.userGuessList[self.indexOfWordToBeGuessed] == self.userGuess:
                    self.indexOfWordToBeGuessed = self.wordToBeGuessed.index(self.userGuess, self.indexOfWordToBeGuessed + 1)
                    self.userGuessList[self.indexOfWordToBeGuessed] = self.userGuess
                else:
                    self.userGuessList[self.indexOfWordToBeGuessed] = self.userGuess
                    
                print(f"The correct guesses and their positions are ---> {self.userGuessList}")
                print(f"The wrong guesses and their positions are ---> {self.wrongGuesses}")
                print("-"*50)
                self.canYouGuessTheWordNow = input("Can you figure out the word now : ")
                if self.canYouGuessTheWordNow == self.wordToBeGuessed:
                    print("Congratulations. . . . . You win. . . . .please play again to guess another interesting word")
                    break
                else:
                    print("Sorry that is not the right word")
                    print(f"The correct guesses and their positions are ---> {self.userGuessList}")
                    print(f"The wrong guesses and their positions are ---> {self.wrongGuesses}") 
                    print("-"*50)
            else:
                print("Sorry, you guessed it wrong.")
                print()
                self.wrongGuesses.append(self.userGuess)
                print(f"The correct guesses and their positions are ---> {self.userGuessList}")
                print(f"The wrong guesses and their positions are ---> {self.wrongGuesses}")
                print("-"*50)
        print("Sorry your man has hung up. . . . . better luck next time")

h = Hangman()
h.startGuessing()


