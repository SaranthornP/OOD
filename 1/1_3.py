print("*** Reading E-Book ***")
Hl,x = input("Text , Highlight : ").split(',')
for i in range(len(Hl)):
    if(Hl[i]==x):
        print('[',x,']',sep='',end='')
    else :
        print(Hl[i],end='')

