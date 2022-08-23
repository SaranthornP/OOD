class StackCalc():
    
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
        
    def size(self):
        return len(self.items)
    
    def run(self,arg):
        s = list(arg.split())
        for i in range(len(s)):
            if s[i] == '+':
                x = float(StackCalc.pop(self))
                y = float(StackCalc.pop(self))
                StackCalc.push(self,x+y)
            elif s[i] == '-':
                x = float(StackCalc.pop(self))
                y = float(StackCalc.pop(self))
                StackCalc.push(self,x-y)
            elif s[i] == '*':
                x = float(StackCalc.pop(self))
                y = float(StackCalc.pop(self))
                StackCalc.push(self,y*x)
            elif s[i] == '/':
                x = float(StackCalc.pop(self))
                y = float(StackCalc.pop(self))
                StackCalc.push(self,x/y)
            elif s[i] == "DUP":
                StackCalc.push(self,self.items[len(self.items)-1])
            elif s[i] == "POP":
                StackCalc.pop(self)
            elif s[i] == "PSH":
                StackCalc.push(self,0)
            elif s[i].isdigit():
                self.items.append(s[i])
            else:
                self.items = "Invalid instruction: " + s[i]
                break
    
    def isEmpty(self):
        return self.items == []
    
    def getValue(self):
        if type(self.items) == list:
            if StackCalc.isEmpty(self) == False :
                return ("{:.0f}".format(float(self.pop())))
            else :
                return 0
        else:
            return self.items
            
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
