class Xox:

    def __init__(self):
        self.playArea = [[1,2,3],[4,5,6],[7,8,9]]
        self.indexOfTheValue = 0
        
    def displayPlayAreaFunc(self):  
        for i in self.playArea:
            print(i) 

    def toFindIndex(self):
        self.whereToPlaceTheValue = int(input("In which place do you want to place your value : "))
        for self.outerIndex in range(len(self.playArea)):
            for self.innerIndex in range(len(self.playArea)):
                if self.whereToPlaceTheValue == self.playArea[self.outerIndex][self.innerIndex]:
                    return self.outerIndex, self.innerIndex         
        else:
            print(f"The place {self.whereToPlaceTheValue} is not empty,choose a different place ")     
            self.toFindIndex()

    def didAnyOneWin(self):
        for i in self.playArea:
            resSet = []
            for j in i:
                resSet.append(j)
            if resSet == ["X","O","X"] or resSet ==  ["O","X","O"]:
                return True
        else:
            return False
                                    
    def game(self):
        for i in range(1,10):
            self.outerIndex, self.innerIndex = self.toFindIndex()
            
            if i % 2 != 0:
                self.playArea[self.outerIndex][self.innerIndex] = "X"
                self.displayPlayAreaFunc()
                # self.DidAnyOneWin()
                resultOfDidAnyOneWin = self.didAnyOneWin()
                if resultOfDidAnyOneWin :
                    print("Congrats player 1, you win")
                    break
            else:
                print(self.outerIndex, self.innerIndex)
                self.playArea[self.outerIndex][self.innerIndex] = "O"
                self.displayPlayAreaFunc()
                # self.DidAnyOneWin()
                resultOfDidAnyOneWin = self.didAnyOneWin()
                if resultOfDidAnyOneWin :
                    print("Congrats player 2, you win")
                    break
    
    
            
x = Xox()
x.displayPlayAreaFunc()
x.game()