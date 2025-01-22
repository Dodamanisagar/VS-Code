import random

def roll():
    min_vslue=1
    max_value=6
    roll=random.randint(min_vslue,max_value)
    return roll

while True:
    players=input("enter the number of players (1-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be in between 2 and 4")
    else:
        print("Invalid, Try again")
print(players)

max_score=50
player_score=[0 for _ in range(players)]


while max(player_score)<max_score:
    for i in range(players):
        print(f"\n Player {i+1}'s turn\n")
        print("your total score is :",player_score[i],"\n")
        current_score=0

        while True:
            should_roll=input("Would you like to roll(Y/N)?")
            if should_roll.lower()!="y":
                break
                
            value=roll()
            if value==1:
                print("You rolled a 1! No points for you!")
                # current_score=0
                break
            else:
                current_score += value
                print("You rolled a",value)

            print("Your current score is",current_score)

        player_score[i]+=current_score
        print("Your total score is",player_score[i])

max_score=max(player_score)
player_win_idx=player_score.index(max_score)
print(f"Player {player_win_idx+1} wins with {max_score} points!")
           
            