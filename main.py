import random
computer = random.choice([-1,0,1])
user = input("Enter s for snake or\nEnter w for water or\nEnter g for gun: ")
userdict={"s":1, "w":-1, "g":0}
reversedict = {1: "snake", -1:"water", 0:"gun"}
you = userdict[user]
print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")
if computer == user:
    print("It's a draw")
else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print('You win!')
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer ==0 and you == 1:
        print("You Lose!")
    else:
        print("Sorry!\nSome Eroor Occurred")