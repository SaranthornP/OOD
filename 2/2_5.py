class funString():
    
    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        x = ""
        for i in range (len(self.string)):
            if ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122 :
                x+=chr(ord(self.string[i])-32)
            elif ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90 :
                x+=chr(ord(self.string[i])+32)
            else :
                x+=self.string[i]
        return x

    def reverse(self):
        x = ""
        for i in range (len(self.string)-1,-1,-1):
            x+=self.string[i]
        return x

    def deleteSame(self):
        x = ""
        for i in range (len(self.string)):
            if self.string[i] not in x:
                x += self.string[i]
        return x



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())