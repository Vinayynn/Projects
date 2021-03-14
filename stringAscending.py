class StringAscending:

    def __init__(self):
        self.s = input("Enter the string here :")
        self.s1 = [None] * len(self.s)
        self.e = 0
        self.s2 =''
    
    def stringFunction(self):
        for i in range(0, len(self.s)):
            self.s1[i] = self.s[i]

        for i1 in range(0, len(self.s)-1):
            for i2 in range(i1+1, len(self.s)):
                if self.s1[i1] > self.s1[i2]:
                    self.e = self.s1[i1]
                    self.s1[i1] = self.s1[i2]
                    self.s1[i2] = self.e

        for each in self.s1:
            self.s2 = self.s2 + each

        print(self.s2)

a = StringAscending()

a.stringFunction()