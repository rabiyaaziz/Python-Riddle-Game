'''In the realm of ancient mysteries, a quest unfolds before you, a journey to uncover five lost relics. With each relic concealed in the heart of enigmatic challenges, 
you are granted three chances to decipher their riddles, or risk losing the game. As you embark on this mystical odyssey, remember, the fate of these relics hangs in the 
balance of your wit and wisdom. Five riddles guard their secrets, and with each triumphant guess, a relic is yours to claim. Yet, the clock of destiny ticks, and failure 
to unlock a riddle's embrace brings defeat. With every riddle you conquer, the ancient relics, with their timeless allure, draw nearer to your grasp. The path is shrouded 
in secrecy, but the reward is immeasurable. Will you accept the challenge and embark on this quest of elegance and intrigue?'''


import random
import time
import sys
import os



# All the necessary functions and variables for the game

def randriddle(): # Function that randomly generates a riddle from the file
  while True:
        try:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(script_dir, 'riddles.txt')
            with open(file_path, "r") as file:
                lines = file.readlines()
                random_riddle = random.choice(lines)
        except FileNotFoundError:
            print("The 'riddles' file is missing. Please make sure it exists in the same directory as the script.")
            sys.exit()

        riddle = random_riddle.strip().split(",")
        if len(riddle) > 1:
            return riddle

used_riddles = set() # set that contains all of the riddles already presented to the user

def get_unique_riddle(): # Function that gets a random riddle but then checks if it has been used before
    while True:
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
            print("Please enter a valid response.")

  
game = True # Condition that checks whether user can continue to keep playing

score = 0 # Score count


# Game starts

print("""\033[1;31;40m
      ╔═════════════════════════════════════════════════╗
      ║ Q U E S T   O F   T H E   L O S T   R E L I C S ║
      ╚═════════════════A Puzzle Game═══════════════════╝
""")
print("\033[1;0m")


rules = '''~~~RULES~~~
You get 3 chances to guess the correct answer.
Your answer MUST be typed out as ONE WORD ONLY. Otherwise, your answers will always be incorrect.
There is a scoring system based on how many tries you take to guess the answer correctly.
You do not get hints. 
'''

name = input("Enter your player name: ")

print(f"Welcome player, {name}. I am the riddlemaster. I understand that you are on a quest to retrieve 5 lost relics. However, it is not something I will give away so easily. ")
print("You will need to prove your wit to me. Answer the following 5 riddles correctly and you will get all 5 relics.")

time.sleep(2)

print(f"\033[1;96;40m {rules}")
print("\033[1;0m")

time.sleep(1)
print("Your adventure begins now...\n")


riddle1 = get_unique_riddle()
print(riddle1[0])

answer1_guess1 = valid_input("You have 3 chances to guess the correct answer. Enter your first guess:")

if answer1_guess1.lower() == (riddle1[1]).lower():
  print(f"Bravo player {name}! You got it right on the first try. Impressive.\nMaybe I underestimated you. Now as part of the deal you can have the first relic.")
  print("\033[93m ** 1 relic obtained **")
  print("\033[1;0m")
  score +=100

else:
  print("Incorrect. You have 2 more chances remaining. Take your time and remember what's at risk.")

  answer1_guess2 = valid_input("Enter your second guess here:")

  if answer1_guess2.lower() == (riddle1[1]).lower():
    print("Good. Now as I promised, you can have the first relic.")
    time.sleep(1)
    print("\033[93m ** 1 relic obtained **")
    print("\033[1;0m")

    score += 50

  else:
    print(f"Think harder. Let me repeat the question:\n{riddle1[0]} Remember, one word answers only.")
    
    answer1_guess3 = valid_input("Enter your final guess here:")

    if answer1_guess3.lower() == (riddle1[1]).lower():
      print("Correct. Alright you can have the first relic. ")
      time.sleep(1)
      print("*** \033[93m 1 relic obtained ***")
      print("\033[1;0m")

      score += 25

    else:
      print(f"Incorrect. Game over. The correct answer is {riddle1[1]} ")
      game = False

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
        print(f"Game over. The correct answer is {riddle2[1]}")
        game = False  

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
        print(f"Game over. The correct answer is {riddle3[1]}")
        game = False



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
        print(f"Game over. The correct answer is {riddle4[1]}")
        game = False

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
        print(f"Game over. The correct answer is {riddle5[1]}")
        game = False

        time.sleep(1)


  if score == 500:
    print(f"Congratulations, {name}! You've obtained all 5 relics and completed the quest!")

    contribute_riddle = input("Would you like to contribute a riddle for future players? (yes/no): ").lower()

    if contribute_riddle == "yes":
      new_riddle_question = valid_input("Enter your riddle: ")
      new_riddle_answer = valid_input("Enter the answer to your riddle: ")

      script_dir = os.path.dirname(os.path.realpath(__file__))
      file_path = os.path.join(script_dir, 'riddles.txt')

      with open(file_path, "a") as file:
        file.write(f"{new_riddle_question},{new_riddle_answer}\n")

      print("Thank you for contributing! Your riddle has been added to the game.")
    else:
      print("Thank you for playing!")

  else:
        print("Thank you for playing!")


print(f"Results for {name}: score = {score}/500.")



