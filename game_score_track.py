import random

def game ():
    print("Welcome to Game !")
    score = yourscore() #score fetched

    print(f"Your Score is {score}")

    with open ("game_highscore.txt") as f:
        hiscore = f.read()

        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    if (score>hiscore):
        with open ("game_highscore.txt", "w") as f:
            f.write(str(score))

def yourscore():
    #taking as random int as no game engine is connected
    score = random.randint(1,100)
    return score

game()