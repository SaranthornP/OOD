class Stack():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def __str__(self):
        st = "Value in Stack = ["
        if Stack.isEmpty(self) == False :
            for i in range(Stack.size(self)):
                st += str(self.items[i])
                if i != Stack.size(self)-1:
                    st += ', '
            st += ']'
            return st
        else :
            st += ']'
            return st
       

    def push(self,i):
        self.items.append(i)  
        return "Add = " + i

    def pop(self):
        if Stack.isEmpty(self) == False:
            num = self.items[Stack.size(self)-1]
            self.items.pop()
            return "Pop = " + num 
        else :
            return "-1"
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return int(len(self.items))
    
    def delete(self,z):
        if Stack.isEmpty(self) == False:
            st = ""
            temp = []
            
            for i in range(Stack.size(self)):
                if int(z) == int(self.items[i]):
                    st += "Delete = " + str(self.items[i]) + '\n'
                else :
                    temp.append(self.items[i])
            if temp == self.items:
                return ''   
            else :
                self.items = temp
                return st   
        else:
            return "-1\n"
    
    def LessThanDelete(self,z):
        if Stack.isEmpty(self) == False:
            st = ""
            temp = []
            t = []
            for i in range(Stack.size(self)):
                if int(z) > int(self.items[i]):
                    t.append(self.items[i])
                else :
                    temp.append(self.items[i])
            if temp == self.items:
                return ''
            else :
                t.sort(reverse=True)
                for i in range(len(t)):
                    st += "Delete = " + str(t[i]) + " Because " + str(t[i]) + " is less than " + z + "\n"
                self.items = temp
                return st 
        else:
            return "-1\n"

    def MoreThanDelete(self,z):
        if Stack.isEmpty(self) == False:
            st = ""
            temp = []
            t = []
            for i in range(Stack.size(self)):
                if int(z) < int(self.items[i]):
                    t.append(self.items[i])
                    
                else :
                    temp.append(self.items[i])
            if temp == []:
                return ''
            else:
                t.sort()
                for i in range(len(t)):
                    st += "Delete = " + str(t[i]) + " Because " + str(t[i]) + " is more than " + z + "\n"
                self.items = temp
                return st
        else:
            return "-1\n"
    
x = list(input("Enter Input : ").split(','))
s = Stack()
for i in range(len(x)):
    y = x[i]
    if y[0]=='P':
        y = x[i][0]
        z = ''
    else:
        y,z = x[i].split()
        
    if y == 'A':
        print(s.push(z))
    
    elif y == 'P':
        print(s.pop())
    
    elif y == 'D':
        print(s.delete(z),end='')
        
    elif y == "LD":
        print(s.LessThanDelete(z),end='')
        
    elif y == "MD":
        print(s.MoreThanDelete(z),end='')
    elif y == 'T':
        for i in range(10):
            print (i)

print(s)

