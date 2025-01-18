
#DESCRIPTION
'''In the realm of ancient mysteries, a quest unfolds before you, a journey to uncover five lost relics. With each relic concealed in the heart of enigmatic challenges, 
you are granted three chances to decipher their riddles, or risk losing the game. As you embark on this mystical odyssey, remember, the fate of these relics hangs in the 
balance of your wit and wisdom. Five riddles guard their secrets, and with each triumphant guess, a relic is yours to claim. Yet, the clock of destiny ticks, and failure 
to unlock a riddle's embrace brings defeat. With every riddle you conquer, the ancient relics, with their timeless allure, draw nearer to your grasp. The path is shrouded 
in secrecy, but the reward is immeasurable. Will you accept the challenge and embark on this quest of elegance and intrigue?'''

#  Modules 
import random # For riddle randomization
import time # Time delays 
import sys #To exit the system if file not found
import os # To get absolute access to the riddles.txt file



# All the necessary functions and variables for the game

def randriddle(): # Function that randomly generates a riddle from the file "riddles.txt"
  while True: # loop
        try:
            script_dir = os.path.dirname(os.path.realpath(__file__)) # This gets the path to the directory where the file is
            file_path = os.path.join(script_dir, 'riddles.txt') 
            with open(file_path, "r") as file:
                lines = file.readlines()
                random_riddle = random.choice(lines)
        except FileNotFoundError: # If the file is not found then an error message is displayed
            print("The 'riddles' file is missing. Please make sure it exists in the same directory as the script.")
            sys.exit() # The system exits

        riddle = random_riddle.strip().split(",")#If the riddle in a file contains a comma between the question & answer, it splits the question and the answer
        if len(riddle) > 1: # If the split riddle contains a question and an answer only then will it be returned
            return riddle

used_riddles = set() # set that contains all of the riddles already presented to the user

def get_unique_riddle(): # Function that gets a random riddle but then checks if it has been used before
    while True: #If the riddle has been used before then the function runs again until it finds one that hasn't been used
        riddle = randriddle()
        if riddle[0] not in used_riddles: # If it hasn't been used before then the riddle is used and added to the used_riddles set
            used_riddles.add(riddle[0])
            return riddle 

def valid_input(prompt): # Checks if the input is not empty
    while True:
        user_input = input(prompt)
        if user_input.strip():  
            return user_input
        else:
            print("Please enter a valid response.") # returns an error message 

  
game = True # Condition that checks whether user can continue to keep playing

score = 0 # Score count




# Game starts

# Title
print("""\033[1;31;40m
      ╔═════════════════════════════════════════════════╗
      ║ Q U E S T   O F   T H E   L O S T   R E L I C S ║
      ╚═════════════════A Puzzle Game═══════════════════╝
""")
print("\033[1;0m")

# Rules for the player
rules = '''~~~RULES~~~
You get 3 chances to guess the correct answer.
Your answer MUST be typed out as ONE WORD ONLY. Otherwise, your answers will always be incorrect.
There is a scoring system based on how many tries you take to guess the answer correctly.
You do not get hints. 
'''

name = input("Enter your player name: ") # Player name

# NPC introduction and dialogue
print(f"Welcome player, {name}. I am the riddlemaster. I understand that you are on a quest to retrieve 5 lost relics. However, it is not something I will give away so easily. ")
print("You will need to prove your wit to me. Answer the following 5 riddles correctly and you will get all 5 relics.")

time.sleep(2) # time delay for added effect

print(f"\033[1;96;40m {rules}")
print("\033[1;0m") # resets color back to default

time.sleep(1)
print("Your adventure begins now...\n")

# Riddle portion
# We decided to do multiple if and else statements instead of a loop so we could include unique dialogue for every attempt

# Riddle 1
riddle1 = get_unique_riddle() # Obtains the riddle by calling the function
print(riddle1[0]) # Only prints the question portion of the riddle

answer1_guess1 = valid_input("You have 3 chances to guess the correct answer. Enter your first guess:")

if answer1_guess1.lower() == (riddle1[1]).lower():
  print(f"Bravo player {name}! You got it right on the first try. Impressive.\nMaybe I underestimated you. Now as part of the deal you can have the first relic.")
  print("\033[93m ** 1 relic obtained **")
  print("\033[1;0m")
  score +=100 # Riddles that are answered correctly on the 1st attempt get 100 points

else:
  print("Incorrect. You have 2 more chances remaining. Take your time and remember what's at risk.")

  answer1_guess2 = valid_input("Enter your second guess here:")

  if answer1_guess2.lower() == (riddle1[1]).lower():
    print("Good. Now as I promised, you can have the first relic.")
    time.sleep(1)
    print("\033[93m ** 1 relic obtained **")
    print("\033[1;0m")

    score += 50 # On the second attempt players get 50 points

  else:
    print(f"Think harder. Let me repeat the question:\n{riddle1[0]} Remember, one word answers only.")
    
    answer1_guess3 = valid_input("Enter your final guess here:")

    if answer1_guess3.lower() == (riddle1[1]).lower():
      print("Correct. Alright you can have the first relic. ")
      time.sleep(1)
      print("*** \033[93m 1 relic obtained ***")
      print("\033[1;0m")

      score += 25 # The third attempt brings them 25 points

    else:
      print(f"Incorrect. Game over.")
      game = False # If they get the answer wrong on all 3 attempts then they cannot go any further. Game is over

# Riddle 2 
if game:

  riddle2 = get_unique_riddle()
  print(riddle2[0])

  answer2_guess1 = valid_input("Enter your first guess here:")

  if answer2_guess1.lower() == (riddle2[1]).lower():
    print(f"Correct. Well done, {name}! Your mind is as sharp as a sword.")
    time.sleep(1)
    print("\033[93m *** 2 relics obtained ***")
    print("\033[1;0m")

    score +=100
  else:
    print("Incorrect. 2 guesses remaining.")

    answer2_guess2 = valid_input("Enter your second guess here:")

    if answer2_guess2.lower() == (riddle2[1]).lower():
      print("Correct. The second relic is yours to claim. ")
      time.sleep(1)
      print("\033[93m *** 2 relics obtained ***")
      print("\033[1;0m")

      score += 50
    else:
      print("Incorrect. The key to the relic may be hidden in the echoes of your thoughts. This is your last chance.")

      answer2_guess3 = valid_input("Enter your third guess here:")

      if answer2_guess3.lower() == (riddle2[1]).lower():
        print("Correct. Whew that was close!")
        time.sleep(1)
        print("\033[93m *** 2 relics obtained ***")
        print("\033[1;0m")

        score += 25

      else:
        print(f"Game over.")
        game = False  

# Riddle 3

if game:
  riddle3 = get_unique_riddle()
  print(riddle3[0])

  answer3_guess1 = valid_input("Enter your first guess here:")

  if answer3_guess1.lower() == (riddle3[1]).lower():
    print("Correct! You're halfway there!")
    time.sleep(1)
    print("\033[93m *** 3 relics obtained ***")
    print("\033[1;0m")

    score += 100

  else:
    print("Incorrect. 2 guesses remaning.")

    answer3_guess2 = valid_input("Enter your second guess here:")

    if answer3_guess2.lower() == (riddle3[1]).lower():
      print("Correct. You're halfway there")
      time.sleep(1)
      print("\033[93m *** 3 relics obtained ***")
      print("\033[1;0m")

      score += 50

    else:
      print("Incorrect. 1 guess remaining")

      answer3_guess3 = valid_input("Enter your third guess here:")

      if answer3_guess3.lower() == (riddle3[1]).lower():
        print("Correct. You're halfway there!")
        time.sleep(1)
        print("\033[93m *** 3 relics obtained ***")
        print("\033[1;0m")

        score += 25
      else:
        print(f"Game over.")
        game = False


# Riddle 4
if game:
  riddle4 = get_unique_riddle()
  print(riddle4[0])

  answer4_guess1 = valid_input("Enter your first guess here:")

  if answer4_guess1.lower() == (riddle4[1]).lower():
    print("Correct! Last relic left to obtain! You're so close!")
    time.sleep(1)
    print("\033[93m *** 4 relics obtained ***")
    print("\033[1;0m")
    score += 100

  else:
    print("Incorrect. 2 guesses remaning.")

    answer4_guess2 = valid_input("Enter your second guess here:")

    if answer4_guess2.lower() == (riddle4[1]).lower():
      print("Correct! Last relic left to obtain! You're so close")
      time.sleep(1)
      print("\033[93m *** 4 relics obtained ***")
      print("\033[1;0m")      
      score += 50

    else:
      print("Incorrect. 1 guess remaining")

      answer4_guess3 = valid_input("Enter your third guess here:")

      if answer4_guess3.lower() == (riddle4[1]).lower():
        print("Correct. Last relic left to obtain! You're so close")
        time.sleep(1)
        print("\033[93m *** 4 relics obtained ***")
        print("\033[1;0m")

        score += 25
      else:
        print(f"Game over.")
        game = False

# Riddle 5
if game:

  print("Only one more challenge stands between you and all the relics. Are you prepared?")

  riddle5 = get_unique_riddle()
  print(riddle5[0])

  answer5_guess1 = valid_input("Enter your first guess here:")

  if answer5_guess1.lower() == (riddle5[1]).lower():
    print("Correct! You did it!")
    time.sleep(1)
    print("\033[93m *** All 5 relics obtained ***")
    print("\033[1;0m")

    score += 100

  else:
    print("Incorrect. 2 guesses remaning.")

    answer5_guess2 = valid_input("Enter your second guess here:")

    if answer5_guess2.lower() == (riddle5[1]).lower():
      print("Correct! You did it!")
      time.sleep(1)
      print("\033[93m *** All 5 relics obtained ***")
      print("\033[1;0m")
      score += 50

    else:
      print("Incorrect. 1 guess remaining")

      answer5_guess3 = valid_input("Enter your third guess here:")

      if answer5_guess3.lower() == (riddle5[1]).lower():
        print("Correct! That was close but you did it!")
        time.sleep(1)
        print("\033[93m *** All 5 relics obtained ***")
        print("\033[1;0m")
        score += 25
        
        

      else:
        print(f"Game over.")
        game = False

        time.sleep(1)


  if score == 500: # If the player gets a perfect score then they have the opportunity to add their own riddle to the game
    print(f"Congratulations, {name}! You've obtained all 5 relics and completed the quest with a perfect score!")

    contribute_riddle = input("Would you like to contribute a riddle for future players? (yes/no): ").lower() 

    if contribute_riddle == "yes":
      new_riddle_question = valid_input("Enter your riddle: ")
      new_riddle_answer = valid_input("Enter the answer to your riddle: ")

      script_dir = os.path.dirname(os.path.realpath(__file__))
      file_path = os.path.join(script_dir, 'riddles.txt')

      with open(file_path, "a") as file:
        file.write(f"{new_riddle_question},{new_riddle_answer}\n") # Adds their riddle to the file

      print("Thank you for contributing! Your riddle has been added to the game.")
    else: # Players have the option to decline and end the game
      print("Thank you for playing!") # Ending message

  else:
        print(f"Congratulations, {name}! You've obtained all 5 relics and completed the quest! Thank you for playing!") # Ending message for players without a perfect score


print(f"Results for {name}: score = {score}/500.") # Shows the score the player got

print("Summary:") # Shows all the riddles asked
for riddle in used_riddles:
      print(riddle)
      time.sleep(1)


# END OF CODE