class Stack():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = len(self.items)
        
    def __str__(self):
        st = Stack.IsValue(self)
        return "Value in Stack = " + st

    def push(self,i):
        self.items.append(i)
        self.size += 1
        return "Add = " + i  + " and Size = " + str(s.size)     

    def pop(self):
        if self.size > 0:
            num = self.items[self.size-1]
            self.items.pop()
            self.size -= 1
            return "Pop = " + num + " and Index = " + str(s.size)
        else :
            return "-1"
    def IsValue(self):
        if self.size > 0 :
            st = ""
            for i in range(self.size):
                st += str(self.items[i]) + ' '
            return st
        else : 
            return "Empty"
        
x = list(input("Enter Input : ").split(','))
s = Stack()
for i in range(len(x)):
    y = x[i]
    if y[0]=='A':
        y,z = x[i].split()
    else:
        y = x[i][0]
        z = ''
    if y == 'A':
        print(s.push(z))
    
    elif y == 'P':
        print(s.pop())

print(s)

