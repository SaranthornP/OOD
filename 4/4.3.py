class Queue():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def __str__(self):
        return str(self.items)
    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
x,lastChar = input("Enter code,hint : ").split(',')
secretCode = Queue()
diff = ord(lastChar) - ord(x[0])
for i in range(len(x)):
    secretCode.enQueue(chr(ord(x[i])+diff))
    print(secretCode)
