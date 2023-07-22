
import random

hard_guess_try = 5
easy_guess_try = 10
#number guessing game objectives


def game():
  print("Welcome to guessing game!")
  print("There is a number I choose between 1 and 100. Would you find it?")
  answer = random.randint(1, 100)
  print(f"{answer}")

  #Let the user guess a number.
  turns = set_difficulty()
  
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attemps remaining to guess the number.")
    guess = int(input("Make a guess:\n"))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You lose.")
      return
# Make function to set difficulty
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or hard:\n")
  if difficulty == 'easy':
    return easy_guess_try
  else:
    return hard_guess_try

#Funciton to check user's guess against actual answer

def check_answer(guess, answer, turns):
  if guess > answer:
    print("High.")
    return turns - 1
  elif guess < answer:
    print("Low.")
    return turns - 1
  else:
    print(f"Congratulations. You found it. Answer is {answer}. ")

  
  
  #Track the number of turns and reduce by 1 if they get it wrong.
  

#repeat it

game()