import random
"""
1 for snake
-1 for water
0 for gun
"""
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youdict[youstr]

print(f"you choose {reversedict[you]}\ncomputer choose {reversedict[computer]}")

if(computer == you):
    print("Its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win!")
    else:
        print("something went wrong!")
   
    
