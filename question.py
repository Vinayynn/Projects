class Question:

    def __init__(self):
        self.questions = [
            "1. Pratheek is the most handsome guy in the class. \n A) YES \n B) No \n C) NO, IT'S VIJAY \n D) BOTH ARE HEROES",
            "2. Vijay will get placed for 20-LPA \n A) YES \n B) No \n C) NO, PRATEEK WILL GET THAT PACKAGE \n D) BOTH WILL GET 20 LPA",
            "3. All girls are mad about pratheek \n A) YES \n B) No \n C) NO, IT'S ON VIJAY \n D) NO, ON BOTH",
        ]

        self.keyAnswers = ["d", "d", "d"]
        self.userAnswers = list()
        self.score = 0

    def displayQuestions(self):
        print("-"*50)
        print("-"*50)
        for each in self.questions:
            print(each)
            print("-"*50)
            self.userAnswers.append(input("Enter your response here : ").lower())
            print("-"*50)
        
    def result(self):
        for each in range(len(self.keyAnswers)):
            if self.userAnswers[each] == self.keyAnswers[each]:
                self.score = self.score + 1
        print("Your score is : ", self.score)
        print("-"*50)

q1 = Question()
q1.displayQuestions()
q1.result()