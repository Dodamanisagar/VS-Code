import random

top_range=input("Type a number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if top_range<=0:
        print("please type a number larger than 0")
        quit()
else:
    print("please type a number next time")
    quit()


random_num=random.randint(0,top_range)#does not inclued top_range 
tries=0
while True:
    tries+=1
    user_guess=input("Make as guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time ")
        continue

    if user_guess==random_num:
        print("you got it right!")
        break
    elif user_guess>random_num:
        print("you were above the number!")
    else:
        print("you were below the number!")
 
print("you got it in",tries,"tries")






