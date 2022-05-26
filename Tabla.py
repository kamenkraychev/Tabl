import random
Dice1 = random.randint(1, 6)
Dice2 = random.randint(1, 6)
print(Dice1)
print(Dice2)
if Dice1 == 6 and Dice2 == 6:
    print("Diushesh")
elif Dice1 == 5 and Dice2 == 5:
    print("Diubesh")
elif Dice1 == 4 and Dice2 == 4:
    print("Dordjar")
elif Dice1 == 3 and Dice2 == 3:
    print("Diuse")
elif Dice1 == 2 and Dice2 == 2:
    print("Diubara")
elif Dice1 == 1 and Dice2 == 1:
    print("Epec")
else:
    print("No Pair")