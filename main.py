import random

#define variables
guess = 0
answer = random.randint(1, 100)

#loop until correct answer is reached
while guess != answer:
    guess = int(input("Please enter your guess between 1 and 100 as an integer: "))

    #give hint as to if its smaller or larger
    if answer > guess:
        print("The answer is larger then that")
    elif answer < guess:
        print("The answer is smaller then that")

#say they got it right
print("Congratulations you got it right!")
