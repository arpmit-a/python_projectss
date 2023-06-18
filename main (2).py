#Number Guessing Game Objectives:

# Include an ASCII art logo.
from art import logo
import random
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.
print("welcome buddy!")
print("We are trying to guess a number between 1 to 100")
level=input("Choose a level. Type 'easy' or 'hard' :")
numtrials=0
if(level=='easy'):
  numtrials=10
elif(level=='hard'):
  numtrials=5
else:
  print('Invalid Input')
list=[i for i in range(1,101)]
numtoguess=random.choice(list)
while(numtrials>0):
  print(f"You have {numtrials} guesses remaining.")
  guess=int(input("make a guess: "))
  if(guess!=numtoguess):
    numtrials-=1
    if(guess<numtoguess):
      print("Too low\n","Guess Again!")
    else:
      print("Too high\n","Guess Again")
  else:
    print("You got it !!")
    print(f"The answer is {numtoguess}")
    break;
if(numtrials==0):
  print(f"You lose. The answer was {numtoguess}")
else:
  print("The end")
  
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

