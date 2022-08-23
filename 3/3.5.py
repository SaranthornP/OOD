class Stack():
    
    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls
            
    def __str__(self):
        return str(self.items)
    
    def push(self,i):
        self.items.append(i)
        
    def pop(self):
        self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def poison(self):
        for i in range(len(self.items)):
            if self.items[i] % 2 == 0 and self.items[i] > 1:
                self.items[i] = self.items[i] - 1
            else:
                self.items[i] = self.items[i] + 2
    
    def check(self):
        x = 0
        count = 0
        for i in reversed(self.items):
            if i > x:
                count += 1
                x = i
            else : continue
        return count
    
x = list(input("Enter Input : ").split(','))
s = Stack()
for i in x:
    if i[0] == 'B':
        print(s.check())
    elif  i[0] == 'S':
        s.poison()
    elif i[0] == 'A':
        z = i.split()
        s.push(int(z[1]))