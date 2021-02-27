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

print('//--------------THIS IS SIMPLE CALCULATOR------------// \n')

x=1
while x>0:
    
    print('\n *********C H O I C E S:********** \n Addition: 1 \n Subtraction: 2 \n Multiplication: 3 \n Division: 4 \n')

    a=int(input(' Enter the first number: '))
    b=int(input(' Enter the second number: '))

    n=int(input(' Enter your choice: '))

    if n==1:
        print(' The sum is : ',add(a,b), '\n')

    elif n==2:
        print(' The difference is : ',sub(a,b), '\n')

    elif n==3:
        print(' The product is : ',mul(a,b), '\n')

    elif n==4:
        print(' The quotient is : ',div(a,b),'\n')

    else:
        print('Invalid inputs')