import time

def add(a,b):
    res=a+b;
    return res

def sub(a,b):
    res=a-b;
    return res

def mul(a,b):
    res=a*b;
    return res

def div(a,b):
    res=a//b;
    return res
def sqr(x):
    res=x**0.5;
    return res    

print('//--------------THIS IS A SIMPLE CALCULATOR------------// \n')

x=1
while x>0:
    
    print('\n ********* C H O I C E S: ********** \n Addition: 1 \n Subtraction: 2 \n Multiplication: 3 \n Division: 4 \n Square Root: 5 \n')
    
    n=int(input(' Enter your choice: '))
    
    if n==5:
        x=int(input(' Enter Number:'))
        print(' The Square Root is : ',sqr(x), '\n')
       
    
    if n==1:
        a=int(input(' Enter the first number: '))
        b=int(input(' Enter the second number: '))

        print(' The sum is : ',add(a,b), '\n')

    if n==2:
        a=int(input(' Enter the first number: '))
        b=int(input(' Enter the second number: '))

        print(' The difference is : ',sub(a,b), '\n')

    if n==3:
        a=int(input(' Enter the first number: '))
        b=int(input(' Enter the second number: '))

        print(' The product is : ',mul(a,b), '\n')

    if n==4:
        a=int(input(' Enter the first number: '))
        b=int(input(' Enter the second number: '))

        print(' The quotient is : ',div(a,b),'\n')
        
time.sleep(1.5)        

    
