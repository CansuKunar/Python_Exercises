# This program checks if the number is prime

def is_prime(number):
    if number <=0:
        print("The negative numbers cannot be prime numbers.")
    else:
        is_prime = True
        if number == 2:
            is_prime = True

        elif number == 1:
            is_prime = False

        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break
        if not is_prime:
            print(f'{number} is not a prime number.')
        else:
            print(f'{number} is a prime number.')

number = int(input('Enter a number: '))
is_prime(number)
