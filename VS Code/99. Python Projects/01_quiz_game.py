print("Welcome to my Computer Quiz!")

# Asking players whethere they wanna play or not
playing=input("Do you want to Play? ")
if playing.lower()!="yes":
    quit()
print("okay! lets paly :)")
score=0

# Asking questions
answer=input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Congratulations! your Answer is Correct")
    score+=1
else:
    print("oops! Wrong Answer")

# Asking questions
answer=input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print("Congratulations! your Answer is Correct")
    score+=1
else:
    print("oops! Wrong Answer")

# Asking questions
answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Congratulations! your Answer is Correct")
    score+=1
else:
    print("oops! Wrong Answer")

# Asking questions
answer=input("What does PSU stand for? ")
if answer.lower()=="power supply unit":
    print("Congratulations! your Answer is Correct")
    score+=1
else:
    print("oops! Wrong Answer")
print("you got",score,"questions correct!")
print("you got", (score/4)*100,"%") 
