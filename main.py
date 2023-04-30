import os
import random
from verbs_database import *

num = 5  #number of challenges per game

# create challenge set from database (list of dicts)
challenge_set = [] #list of dicts
challenge_set = random.sample(verbs, num) 

# some repetitive functions
def clear():
  for l in range(12):
    print()

def press(type):
  input("\nPress enter to " + type + " ...")

def intro():
  print("\n\n=============================")

def outro():
  print("=============================\n\n")

current = 0
game = True

# intro text
intro()
print("Welcome to the German verb game!")
outro()
press("continue")
clear()
intro()
print("This is how it works.\nI'll give you a present tense verb\nat the A1-A2 level.\n")
print("Like so: machen\n")
press("continue")
clear()
intro()
print("You will then type out the \npast (p) & past perfect tense (pp) \nforms in the 3rd person.\n")
print("Like so:\nWhat is the p?\nmachte\nWhat is the pp? (with hat or ist)\nhat gemacht\n")
press("continue")
clear()
intro()
print("If you answer correctly,\nyou'll move forward,\nbut if you get it wrong,\nyou'll have to go back one step.\n\nFinish all 5 challenges to win.\nEach time you open up the game,\nit'll be a new\nrandom set of challenges\nfrom a database of 100 words!\n"
)
press("continue")
clear()
intro()
print("Klingt gut? Let's do this then!")
outro()
press("start the game")
clear()  #refresh screen by adding lines

#start game loop
while game:

  #first challenge
  intro()
  print("You are now at challenge " + str(current + 1) + "/" +
        str(len(challenge_set)))
  outro()

  #the verb
  print("Here's the verb: " + challenge_set[current]["verb"] + "\n (" + challenge_set[current]["English"] + ")\n")

  #ask for input
  p = input("What is the p?" + "\n" * 4 + "\033[3A").strip().lower()
  pp = input("\nWhat is the pp? (with hat or ist)"+ "\n" * 4 + "\033[3A").strip().lower()

  # when correct
  if (p == challenge_set[current]["p"] and pp == challenge_set[current]["pp"]):
    current += 1 #move to next challenge
    print("\nCorrect!!!!!\n")
    if current == len(challenge_set):  #reach the end
      clear()
      intro()
      print("Congrats! You won the game!\n omgomg")
      outro()
      press("end the game")
      game = False
    else:
      print("Next challenge.")
      press("continue")
      clear()

  # when incorrect
  else:
    print("\nIncorrect! Back you go!\n")
    print("The answers: ")
    print(challenge_set[current]["p"])
    print(challenge_set[current]["pp"])
    press("continue")
    clear()

    current -= 1
    if current < 0:  #if reach beginning, start from there
      current = 0
    else:
      current

print("Come back again to practice more verbs.\n\n\nDeveloped by Lynn Chiu 2023")
