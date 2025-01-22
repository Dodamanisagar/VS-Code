name=input("Type your name ")
print("welcome",name,"to your adventure!")

answer=input("Your are on a  dirt road. it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer=="left":
    answer= input("you came to river, you can walk arround it or swim across? what you would select swim or walk ").lower()
    if answer=="swim":
        print("You swim across and were eaten by alligator")
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not valid option. You lose.")

elif answer== "right":
    answer= input("you came to bridge, it looks wobbly, do you want to cross or want to go back ").lower()
    if answer=="back":
        print("you walked back and lose")
    elif answer=="cross":
        answer=input("you crossed the bridge and meet the stranger , do you want to talk with them. Yes or No? ").lower()
        if answer=="yes":
            print("you talked talked with stranger and he guided you to the main route")
        elif answer=="no":
            print("You wwnt without talking with stranger and lost again")
        else:
            print("Not a valid option. you lose")
    else:
        print("Not valid option. You lose.")
else:
    print("Not valid option. You lose.")
print("Thank you for trying")