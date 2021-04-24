import random

random_number=random.randint(1,3)

if random_number==1:
    computer='s'
elif random_number==2:
    computer='w'
elif random_number==3:
    computer='g'

you=input("Your Turn: Snake(s) Water(w) Gun(g)?")

def game_win(you,computer):
    if computer==you:
        return None
    elif computer=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif computer=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif computer=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


a=game_win(you,computer)

print(f"Computer choosed {computer}")
print(f"You choosed {you}")

if a==None:
    print("The game is a tie")
elif a:
    print("Horray!You Won the game")
else:
    print("You lost the game")