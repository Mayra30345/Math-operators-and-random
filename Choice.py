import random
options=["Rock","Paper","Scissors"]
user=input("Choose between Rock,Paper and Scissors  ")
computer=random.choice(options)
print("You choose: ",user)
print("Computer's choose: ",computer)
if user==computer:
    print("Its a tie!")
elif user=="Rock" and computer=="Scissors":
    print("You win as the rock smashes the scissors")
elif user=="Paper" and computer=="Rock":
    print("You win as the paper covers the rock")
elif user=="Scissors" and computer=="Paper":
    print("You win as the scissors cut through paper")
else:
    print("You lose")