class Stack():
    
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls
            
    def push(self,i):
        self.items.append(i)
        
    def pop(self):
        num = self.items[len(self.items)-1]
        self.items.pop()
        return num
        
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def postFixeval(st):

    s = Stack()

    for i in range(len(st)):
        if st[i] == '+':
            x = float(s.pop())
            y = float(s.pop())
            s.push(x+y)
        elif st[i] == '-':
            x = float(s.pop())
            y = float(s.pop())
            s.push(y-x)
        elif st[i] == '*':
            x = float(s.pop())
            y = float(s.pop())
            s.push(x*y)
        elif st[i] == '/':
            x = float(s.pop())
            y = float(s.pop())
            s.push(y/x)
        else :
            s.push(st[i])
    
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))