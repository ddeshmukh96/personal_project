""""
The game() function in a program let a user play game and returns
the score as an integer . You need to read a file 'Hi-score.txt'
which is either blank or contains the previous Hi-score. You need
to write a program to update the Hi-score whenever the game() function
breaks the Hi-score.

"""

import random

def game():

    print("You are playing the game")

    score=random.randint(0,100)

    with open("high_score.txt","r") as f:

        content=f.read()

        if content!="":
            high_score=int(content)
        
        else:
            high_score=0

    if score>high_score:

        with open("high_score.txt","w") as f:
            f.write(str(score))
    
    return f"Your score : {score}"

print(game())