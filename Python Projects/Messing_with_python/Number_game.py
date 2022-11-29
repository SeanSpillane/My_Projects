import random

guess = 0

def get_number():
    guess = int(input('enter a number between 1 and 100: '))

number = int(random.randrange(1,100))

running = True

while running:
    get_number()
    
    if guess == number:
        print(f'{number} was the correct answer!')

    elif guess < number:
        print('the number is higher than that')

    elif guess > number:
        print('the number is lower than that')



    
    

    
        


