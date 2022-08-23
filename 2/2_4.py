Num = list(str(input("Enter Your List : ")).split(' '))
x = []
c = 0
if(len(Num)>=3):
    print('[',end='')
    for i in range (len(Num)):
        for j in range (i+1,len(Num),1):
            for k in range (j+1,len(Num),1):
                if int(Num[i]) + int(Num[j]) + int(Num[k]) == 0 :
                   
                    xtemp = x
                    x = [Num[i] , Num[j] , Num[k]]
                    if( xtemp == x) :
                        break
                    else : xtemp = x
                    if(c!=0):
                        print(", ",end='')
                    print('[',x[0] ,', ', x[1] ,', ', x[2],']',sep='',end='')
                    c = 1
                    
    print(']')
else :
    print("Array Input Length Must More Than 2")