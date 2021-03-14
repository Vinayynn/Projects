from datetime import *

class Chat:
    def __init__(self):
        self.nameOfFirstPerson = input("Hey! person 1. May I know your name please? :")
        self.nameOfSecondPerson = input("Hey! person 2. May I know your name please? :")
        self.messageFromFirstPerson = ""
        self.messageFromSecondPerson = ""

    def replyToMessages(self):
        print("-"*50)
        for each in range(1, 20):
            if each % 2 != 0 :
                self.messageFromFirstPerson = input("{}, Type your message to {} here :".format(self.nameOfFirstPerson, self.nameOfSecondPerson))
                print("-"*50)
                print("Message from : {}".format(self.nameOfFirstPerson))
                print()
                print("     {}".format(self.messageFromFirstPerson))
                print()
                print("     sent at :", datetime.now())
                print("-"*50)
            else:
                self.messageFromSecondPerson = input("{}, Type your message to {} here :".format(self.nameOfSecondPerson, self.nameOfFirstPerson))
                print("-"*50)
                print("Message from : {}".format(self.nameOfSecondPerson))
                print()
                print("     {}".format(self.messageFromSecondPerson))
                print()
                print("     sent at :", datetime.now())
                print("-"*50)


c1 = Chat()
c1.replyToMessages()