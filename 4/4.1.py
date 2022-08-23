class Queue():
    
    def __init__(self,list = None):
        if list == None:
            self.items = []
            self.temp = []
        else:
            self.items = list
            self.temp = []
    
    def enQueue(self,i):
        self.items.append(i)
        
    def deQueue(self):
        temp = self.items.pop(0)
        self.temp.append(temp)
        return temp
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
x = list(input("Enter Input : ").split(','))
q = Queue()
for i in x:
    if i[0] == 'E':
        y = i.split()
        q.enQueue(y[1])
        s = ""
        for i in range(q.size()):
            s += str(q.items[i])
            if i < q.size() - 1:
                s += ', '
        print(s)
    elif i[0] == 'D':
        if q.isEmpty() == False:
            s = str(q.deQueue()) + " <- "
            if q.isEmpty() == False:
                for i in range(q.size()):
                    s += str(q.items[i])
                    if i < q.size() - 1:
                        s += ', '
            else:
                s += "Empty"
            print(s)
        else:
            print("Empty")
            
if q.isEmpty() == False:
    if q.temp == []:
        print("Empty :",', '.join(q.items))
    else:
        print(', '.join(q.temp) ,':',', '.join(q.items))
elif q.temp != []:
    print(', '.join(q.temp) ,': Empty')
else:
    print('Empty : Empty')
            