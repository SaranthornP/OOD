from cgitb import reset


print("*** multiplication or sum ***",end='\n')
num1,num2 = [int(x) for x in input("Enter num1 num2 : ").split()]
Result = num1*num2
if(Result>1000):
    print("The result is",num1+num2)
else:
    print("The result is",num1*num2)
