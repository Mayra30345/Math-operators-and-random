import random
number= (random.randint(10,20))
print("I will generate a number from 10 to 20 and You have to guess it!")
print("The game will end when you win atleast one time")
while True:
    guess=int(input("Give me your best guess!"))
    if number==guess:
        print("You won!")
        print("The number was",number)
        break
else:
    print("Try again\n")