# pythagorean triple flash card thing?
import random

# all real and fake triples used being placed into an index
realTriples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
               (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
               (11, 60, 61), (16, 63, 65), (33, 56, 65), (48, 55, 73),
              (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]

fakeTriples = [(3, 4, 6),(5, 5, 10),(8, 15, 25),
              (12, 18, 30),(7, 24, 36),(10, 11, 21),
              (14, 28, 42),(9, 40, 45),(11, 60, 61),
              (20, 21, 22),(8, 15, 16),(12, 18, 20),
              (14, 21, 28),(10, 24, 26),(16, 30, 40),
              (22, 33, 44),(9, 12, 20),(14, 22, 29),
              (20, 25, 30),(7, 11, 14),(6, 10, 13),
              (9, 15, 20),(11, 22, 27),(13, 26, 31),
              (17, 34, 39),(8, 16, 24),(18, 27, 36),
              (25, 35, 45),(12, 16, 22),(23, 30, 40)]

# Used to keep score of real and fake triples and the score of answers that either are correct or wrong.
score =  [0,0]
realANDfake = [0,0]
# Used for the while loop statement.
x = 0

# Introduction to the program, giving an overview and instructions.
print("Welcome to the Pythagorean triples flash cards!")
print("Rules: ")
print("If it is a Pythagorean triple (press y)")
print("If it isnt a Pythagorean triple (press n)")
print("")
print("Please enter how many Pythagorean triples you want to do? ") 

# Asks the user how many triples the user wants to be given. This also makes sure the user input is a integer and not a character(s).
while True:
  try:
    amount = int(input("Enter an integer number: "))
    break
  except ValueError:
        print("Please input integer only")  
        continue

# This creates a function that checks if the input is either n or y and if it matches the given character for x then the user is correct and their score increases.
def check(x):
    if input() == x:
            print ("It is a Pythagorean triple CONGRATS!")
            score[0] = score[0] + 1
    else:
        print("It is not a Pythagorean triple. ):")
        score[1] = score[1] + 1
    print("")

# while statement in order to give the amount of triples the user wants.   
while (x != amount):
    if random.randint(1,2) == 1:
        # Keeps track of the amount of real and fake triples, it also finds a "random" triple from the list. Calling the function above in order to verify
        # if the user is correct. 
        realANDfake[0] = realANDfake[0] + 1
        print("Is this a Pythagorean triple: " + str(realTriples[int(random.randint(0,15))]))
        check("y")
        x = x + 1
    else:
        realANDfake[1] = realANDfake[1] + 1
        print("Is this a Pythagorean triple: " + str(fakeTriples[int(random.randint(0,15))]))
        check("n")
        x = x + 1

# Gives the user it's score and the amount of fake and real triples given.
print("You got " + str(score[0]) + " correct and " + str(score[1]) + " wrong." + " You got a score of " + str((int(score[0])/amount)*100) + "% !")
print("There was " + str(realANDfake[0]) + " Pythagorean triple(s) and " + str(realANDfake[1]) + " fake(s).")
print("Press enter to exit the program.")
# When the user presses enter it exits the program
input()
