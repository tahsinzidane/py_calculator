def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def devide(x,y):
    if y != 0:
        return y / x
    else:
        return 'connot devide by zero'
    
print('select option')
print('1. add')
print('2. minus')
print('3. multiply')
print('4. devide')

choice = int(input('inter your option: ' ))
print(f'You have chosen option {choice}')

num1 = int(int(input('enter your first int number: ' )))
num2 = int(int(input('enter your second int number: ' )))

if choice == 1:
    print(f'{num1} + {num2} = {add(num1, num2)}')
elif choice == 2:
    print(f'{num1} - {num2} = {minus(num1, num2)}')
elif choice == 3:
    print(f'{num1} * {num2} = {multiply(num1, num2)}')
elif choice == 4:
    print(f'{num1} / {num2} = {devide(num1, num2)}')
else:
    print('invalid input')
    

