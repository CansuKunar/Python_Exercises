import random

print('Welcome to the guess game\nDo you want 5 tickets or more?')
version = int(input('If 5 tickets are enough, enter the 1; if you want more enter the number 2: '))

# Version 1
if version == 1:
    x = random.randrange(0, 100, 1)
    ticket = 0
    point = 100
    number = int(input('Enter your guess(0 to 100): '))

    while ticket <= 5:
        if ticket >= 5:
            print('Sorry You lose :(')
            print(x)
            break
        else:
            if number == x:
                print(f'Congratulations! You found the right number. Your point is {point}')
                break
            elif number > x:
                number = int(input('Enter a smaller number: '))
                ticket += 1
                point -= 20
            else:
                number = int(input('Enter a larger number: '))
                ticket += 1
                point -= 20

# Version 2
elif version == 2:
    x = random.randrange(0, 100, 1)
    total_ticket = int(input('How many tickets would you like? : '))
    ticket = 1
    point = 100
    number = int(input('Enter your guess(0 to 100): '))
    while ticket <= total_ticket + 1:
        if ticket == total_ticket + 1:
            print('Sorry You lose :(')
            break
        else:
            if number == x:
                print(f'Congratulations! You found the right number. Your point is {point}')
                break
            elif number > x:
                number = int(input('Enter a smaller number: '))
                ticket += 1
                point -= (100 / total_ticket)
            else:
                number = int(input('Enter a larger number: '))
                ticket += 1
                point -= (100 / total_ticket)
                
else:
    print("You entered the wrong number.")