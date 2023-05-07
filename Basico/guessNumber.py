import random

def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Adivina el número entre 1 y {x}: "))
        if guess < rand_num:
            print("Muy bajo")
        elif guess > rand_num:
            print("Muy alto")
    
    print(f"Felicidades, adivinaste el número {rand_num} correctamente")


guess(15)
            
