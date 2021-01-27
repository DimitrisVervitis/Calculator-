print (30 * '-')
print('    C A L C U L A T O R')
print (30 * '-')
print ("    M A I N - M E N U")
print (30 * '-')
print ("1. Addition +")
print ("2. Subtraction -")
print ("3. Proliferation *")
print ("4. Division /")
print (30 * '-')

choice=int(input(' Enter your choice [1-4] : '))

number1=float(input('Enter your first number : '))
number2=float(input('Enter your second number : '))

if choice==1:
    print(number1+number2)
elif choice==2:
    print(number1-number2)
elif choice==3:
    print(number1*number2)
else:
    print(number1/number2)
