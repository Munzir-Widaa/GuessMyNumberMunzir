import random
#program picks a random number between 1 and 6
random_number = random.randint(1, 6)
#gets number from user
user_guess = int(input("Guess a number between 1 and 6: "))
#if the user number is the same as computer number then its right otherwise its wrong
if user_guess == random_number:
  print("You guessed right")
else:
  print("You gussed wrong")