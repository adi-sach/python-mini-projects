from random import randint

x=randint(1,10)
attempts = 0
y=-1
while (x!=y):
    attempts+=1
    y=int(input("Enter a number between 1 & 10 \n"))

    if (y>0 and y<11):

        if (x<y):
            print("Lower number please")
        elif (y<x):
            print("Higher number please")
    else:
        print("invalid input")
print(f"You took {attempts} number of tries to reach the number")

