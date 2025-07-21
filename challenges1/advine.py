import random
randome = random.randint(1, 100)
chance = int(input("Enter the number: "))
while chance != randome:
    chance = int(input("Enter the number: "))
print(f"Congratulations!! The random number is: {randome}")