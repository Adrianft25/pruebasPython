import random

def play():
    user = input("Piedra, Papel o Tijera:" + "\n" + "R. Piedra" + "\n" + "P. Papel" + "\n" + "T. Tijera" + "\n")
    ia = random.choice(["r", "p", "t"])

    if  user == ia:
        return "Empate"
    
    if is_win(user, ia):
        return "Ganaste"
    
    return "Perdiste"

def is_win(user, ia):
    if (user == "r" and ia == "t") or (user == "p" and ia == "r") or (user == "t" and ia == "p"):
        return True
    
print(play())