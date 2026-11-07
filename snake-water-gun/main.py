'''
1 for snake
-1 for water
0 for gun

'''


import random

computer=random.choice([-1, 0, 1])
you=input("Enter your choice ")
dict={ "s":1, "w":-1, "g":0}
revDict={ 1:"Snake", -1:"Water", 0:"Gun"}
You=dict[you]

print(f"You chose {revDict[You]}")
print(f"Computer chose {revDict[computer]}")

if (computer == You):
    print("It's a draw")

else:
    if(computer ==1 and You==-1):
        print("Computer Won!")
    elif(computer ==1 and You==0):
        print("You Won!")
    elif(computer ==0 and You==-1):
        print("You Won!")
    elif(computer ==0 and You==1):
        print("Computer Won!")
    elif(computer ==-1 and You==0):
        print("Computer Won!")
    elif(computer ==-1 and You==1):
        print("You Won!")
    else:
        print("Something went wrong")