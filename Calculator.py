import math 
print (30 * '-')
print('    C A L C U L A T O R')
print (30 * '-')
print ("    M A I N - M E N U")
print (30 * '-')
print ("1. Addition +")
print ("2. Subtraction -")
print ("3. Proliferation *")
print ("4. Division /")
print ("5. Square ")
print (30 * '-')

choice=int(input(' Enter your choice [1-5] : '))

if choice==5:
    number1=float(input('Enter your number you want to square : '))
    Square=math.sqrt(number1)
    print(Square)
elif choice==1:
    number2=float(input('Enter your first number : '))
    number3=float(input('Enter your second number : '))
    print(number2+number3)
elif choice==2:
    number2=float(input('Enter your first number : '))
    number3=float(input('Enter your second number : '))
    print(number2-number3)
elif choice==3:
    number2=float(input('Enter your first number : '))
    number3=float(input('Enter your second number : '))
    print(number2*number3)
else:
    number2=float(input('Enter your first number : '))
    number3=float(input('Enter your second number : '))
    print(number2/number3)
    
