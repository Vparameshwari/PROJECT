import random

name1 = input("Enter the player1 name: ")
name2 = input("Enter the player2 name: ")

d1 = random.randint(1, 25)
d2 = random.randint(1, 25)

s1 = 25
s2 = 25

print("-------PLAYER 1 HAS TO GUESS--------")

while True:
    g1 = int(input("Enter your guess: "))
    if d1 == g1:
        print("THE GUESS IS CORRECT")
        break
    elif d1 < g1:
        print("YOUR GUESS IS HIGH")
    else:
        print("YOUR GUESS IS LOW")
    s1 = s1 - 1

print("-------PLAYER 2 HAS TO GUESS--------")

while True:
    g2 = int(input("Enter your guess: "))
    if d2 == g2:
        print("THE GUESS IS CORRECT")
        break
    elif d2 < g2:
        print("YOUR GUESS IS HIGH")
    else:
        print("YOUR GUESS IS LOW")
    s2 = s2 - 1

if s1 > s2:
    print(name1, "won")
elif s2 > s1:
    print(name2, "won")
else:
    print("It's a tie")
