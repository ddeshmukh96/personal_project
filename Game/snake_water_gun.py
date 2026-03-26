import random

"""
Snake = 0
Gun = 1
Water = 2

sys = 0  player = 2
Snake drinks the water so sys wins

sys = 1  player = 0
Gun kills the snake so sys wins

sys = 2  player = 1
Water sinks the gun so sys wins

"""

def snake_water_gun(system,player):
    
    if system == player:
        return 0
    
    elif system == 0 and player == 2:
        return -1
    
    elif system == 1 and player == 0:
        return -1
    
    elif system == 2 and player == 1:
        return -1
    
    return 1

choices=['Snake','Gun','Water']

trial=1
system_score=0
player_score=0

while trial<=5:
    
    player_input=input(f"Round {trial} of 5.\nEnter your choice\n0 = Snake\n1 = Gun\n2 = Water\nType 'quit' to exit the game: ")
    
    if player_input.strip().lower()=='quit':
        print("Game exited!\nThanks for Playing!")
        break
    
    if not player_input.isdigit():
        print("Invalid input!\nPlease choose 0 1 2 or 'quit'.")
        continue
    
    player=int(player_input)
    
    if player not in [0,1,2]:
        print("Invalid choice!\nTry again\n")
        continue
    
    system=random.randint(0,2)

    result=snake_water_gun(system,player)

    print(f"The system chose {choices[system]} and player chose {choices[player]}")

    if  result == 0:
        print("Match Draw")
    elif result == -1:
        print("You Lose!")
        system_score+=1
    else:
        print("You Win")
        player_score+=1
    
    trial+=1
    print()

print(f"System Scores: {system_score} | Player scores: {player_score} ")

if player_score>system_score:
    print("🎉 You won the series!")
elif player_score<system_score:
    print("😢 System won the series!")
else:
    print("🤝 Series Draw")