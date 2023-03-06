# This program finds prime numbers between two numbers.

def is_prime(num1, num2):
    for num in range(num1, num2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        
        else:
            print("You entered the wrong number.")
            break
        

def get_number():
    number1 = int(input('Enter the first number(number > 1): '))
    number2 = int(input('Enter the last number: '))
    if (number1 < 1) and (number2 < 1):
        print("The numbers cannot be negative. ")
        return 0, 0
    elif number2 <= number1:
        print("The last number cannot be less than or equal to the first number.")
        return 0, 0
    return number1, number2

print("Please enter two number.")

num1, num2 = get_number()

is_prime(num1, num2)