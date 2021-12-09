import random
import replit
from art import tprint
"""
This code is for the game hangman, in which someone must guess
something from a category with a limited amount of guesses.
"""



#----------------------------------------------------------------------
def choose_word():
  category = input("Choose a category from the following: Movies, Sports, Foods: ")
  while category != "movies" and category != "sports" and category != "foods" and category != "Movies" and category != "Sports" and category != "Foods":
    print("Not an input.")
    category = input("\nWhat would you like to do?: ")

    
  if category == "Movies" or category == "movies":
    movie_choice = [ 'rocky', 'joker', 'avatar', 'psycho', 'alien', 'scarface', 'inception', 'parasite', 'whiplash', 'gladiator', 'avengers', 'batman', 'hamlet', 'jaws', 'aladdin', 'matrix', 'venom', 'baywatch', 'cars', 'terminator', 'titanic', 'godfather']  
    game_word = random.choice(movie_choice)
    print(str(len(game_word)) + " letters in the word")
  elif category == "Sports" or category == "sports":
    sports_choice = ['basketball', 'football', 'baseball', 'hockey', 'soccer', 'cricket', 'tennis', 'volleyball', 'rugby', 'golf', 'swimming', 'bowling', 'boxing', 'archery', 'curling']  
    game_word = random.choice(sports_choice)
    print(len(game_word) + "letters in the word-")
  elif category == "Foods" or category == "foods":
    foods_choice = ['pizza', 'corn', 'pasta', 'potato', 'rice', 'avocado', 'pancake', 'bread', 'broccoli', 'cheese', 'burrito', 'cereal', 'carrot', 'onion', 'apple', 'banana', 'sandwich', 'steak', 'burger', 'oatmeal', 'strawberry']  
    game_word = random.choice(foods_choice)
 
    print(str(len(game_word)) + " letters in the word-")
  return game_word

#----------------------------------------------------------------------
def player_guess(game_word):
  turn = 1
  guesses = ""
  wrong_guess = ""
  while turn > 0: 
    
    fails = 0
    for char in game_word:
      
      if char in guesses:
         print(char, end="")
         
      else: 
        print("_", end="") 
        fails = fails + 1
    
    if fails == 0:
      print("\n\nCONGRATULATIONS, YOU WIN!")
      break
      
    guess = input(" Choose a letter: ")
    guesses += guess 
    if guess not in game_word:
      wrong_guess += guess
      turn = turn - 1
      print("Wrong")
      print("Turns left: " + str(turn))
      print("Letters guessed: ", end="")
      for letter in wrong_guess:
        print((letter), end=", ")
      print()
      if turn == 0:
        print("\nYOU LOSE")
        break

#------------------------------------------------------------------------------------
def menu():
  game_type = None
  tprint("HANGMAN", "Boxing")
  print("Welcome to Hangman! \n" )
  print("_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._")
  print("\n\nMenu-Options: \n\n [1]Single Player  [2]Multiplayer  [3]Versus AI ")
  try:
    game_type = int(input("\nWhat would you like to do?: "))
  except:
    print("Not an input.")
  
  
  replit.clear()
  return game_type
#--------------------------------------------------------------------------------------
def player(allturn):
  print("Welcome to multiplayer!")
  print("\nIn this mode, 2 players will go head to head in a 1v1 hang man battle.\n Player 1 will go first.")
    
  category = input("\nChoose a category from the following: Movies, Sports, Foods: ")
      
  if category == "Movies" or category == "movies":
    movie_choice = [ 'rocky', 'joker', 'avatar', 'psycho', 'alien', 'scarface','inception', 'parasite', 'whiplash', 'gladiator', 'avengers', 'batman', 'hamlet', 'jaws', 'aladdin', 'matrix', 'venom', 'baywatch', 'cars', 'terminator', 'titanic', 'godfather']  
    game_word = random.choice(movie_choice)
  elif category == "Sports" or category == "sports":
   sports_choice = ['basketball', 'football', 'baseball', 'hockey', 'soccer', 'cricket', 'tennis', 'volleyball', 'rugby', 'golf', 'swimming', 'bowling', 'boxing', 'archery', 'curling']  
   game_word = random.choice(sports_choice)
  elif category == "Foods" or category == "foods":
    foods_choice = ['pizza', 'corn', 'pasta', 'potato', 'rice', 'avocado', 'pancake', 'bread', 'broccoli', 'cheese', 'burrito', 'cereal', 'carrot', 'onion', 'apple', 'banana', 'sandwich', 'steak', 'burger', 'oatmeal', 'strawberry']
    game_word = random.choice(foods_choice)
  player_1 = True
  while True:  
    if player_1:
      player_1_turn = 10
      guesses = ""
      wrong_guess = ""
      while player_1_turn > 0: 
        
        fails = 0
        for char in game_word:
          
          if char in guesses:
            print(char, end="")
            
          else: 
            print("_", end="") 
            fails = fails + 1
        
        if fails == 0:
          print("\n\nCONGRATULATIONS, You finished!")
          break
          
        guess = input(" Choose a letter: ")
        guesses += guess 
        if guess not in game_word:
          wrong_guess += guess
          player_1_turn = player_1_turn - 1
          print("Wrong")
          print("Turns left: " + str(player_1_turn))
          print("Letters guessed: ", end="")
          for letter in wrong_guess:
            print((letter), end=", ")
          print()
          if player_1_turn == 0:
            print("\nYou ran out of turns.")
            break
      print("Player 1 Used " + str(10 - player_1_turn) + " Turns")
      replit.clear()
      player_1 = False
    else: 
      player_2_turn = 10
      guesses = ""
      wrong_guess = ""
      while player_2_turn > 0: 
        
        fails = 0
        for char in game_word:
          
          if char in guesses:
            print(char, end="")
            
          else: 
            print("_", end="") 
            fails = fails + 1
        
        if fails == 0:
          print("\n\nCONGRATULATIONS, You finished!")
          break
          
        guess = input(" Choose a letter: ")
        guesses += guess 
        if guess not in game_word:
          wrong_guess += guess
          player_2_turn = player_2_turn - 1
          print("Wrong")
          print("Turns left: " + str(player_2_turn))
          print("Letters guessed: ", end="")
          for letter in wrong_guess:
            print((letter), end=", ")
          print()
          if player_2_turn == 0:
            print("\nYou ran out of turns.")
            break
      print("Player 1 Used " + str(10 - player_2_turn) + " Turns")
      
    break
  allturns = [player_1_turn, player_2_turn]
  return allturns
#------------------------------------------------------------------------------------



allturn = None
game_type = menu()


while game_type != 1 and game_type != 2 and game_type != 3:
  print("Not an input.")
  try:
    game_type = int(input("\nWhat would you like to do?: "))
  except:
    print("\nIncorrect; Please select the game type.")

if game_type == 1:
  game_word = choose_word()
  player_guess(game_word)

elif game_type == 2: 
  player(allturn)
  allturn = player(allturn)
  player_1_turn = allturn[0]
  player_2_turn = allturn[1]

  

  if player_1_turn > player_2_turn:
    print("\033[1;32;40mPlayer 1 wins!")

  elif player_2_turn > player_1_turn:
    print("\033[1;32;40mPlayer 2 wins!")

  elif player_1_turn == player_2_turn :
    print("\033[1;32;40mIts a tie!")