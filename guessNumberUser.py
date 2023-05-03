import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Es {guess} muy alto (A), muy bajo (B), o correcto (C)??').lower()
        if feedback == 'a':
            high = guess - 1
        elif feedback == 'b':
            low = guess + 1
    
    print(f'Adiviné, el número es {guess}!')

computer_guess(1000)