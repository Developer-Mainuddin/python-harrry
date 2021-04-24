def game():
    return 5555

score=game()

with open('highscore.txt','r') as file:
    highscore_str=file.read()

if highscore_str=='':
    with open('highscore.txt','w') as file:
        file.write(str(score))
elif score>int(highscore_str):
    with open('highscore.txt','w') as file:
        file.write(str(score))
        
