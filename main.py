import random
import replit
from art import tprint
"""
This code is for the game hangman, in which someone must guess
something from a category with a limited amount of guesses.
"""



#---------------------------------------------------------------------------------------
"""
This segment of code asks the user for a category, randomly chooses an option based
on their input, and tells the user how many letters are in the word.
"""

def choose_word():
  #Asks the user for a category.
  category = input("Choose a category from the following: Movies, Sports, Foods: ")
  
  #If input isn't movies, sports, or foods.
  while category != "movies" and category != "Movies"  and category!= "Sports" and category != "sports" and category != "Foods" and category != "foods":
    print("Not an input, try again.")
    category = input("\nChoose a category from the following: Movies, Sports, Foods: ")
  
  #Randomly picks an option if the input was "movies".
  if category == "Movies" or category == "movies":
    movie_choice = [ 'rocky', 'joker', 'avatar', 'psycho', 'alien', 'scarface', 'inception', 'parasite', 'whiplash', 'gladiator', 'avengers', 'batman', 'hamlet', 'jaws', 'aladdin', 'matrix', 'venom', 'baywatch', 'cars', 'terminator', 'titanic', 'godfather','spider-man','']  
    game_word = random.choice(movie_choice)
    print(str(len(game_word)) + " letters in the word")

  #Randomly picks an option if the input was "sports".
  elif category == "Sports" or category == "sports":
    sports_choice = ['basketball', 'football', 'baseball', 'hockey', 'soccer', 'cricket', 'tennis', 'volleyball', 'rugby', 'golf', 'swimming', 'bowling', 'boxing', 'archery', 'curling']  
    game_word = random.choice(sports_choice)
    print(str(len(game_word)) + " letters in the word")

  #Randomly picks an option if the input was "foods".
  elif category == "Foods" or category == "foods":
    foods_choice = ['pizza', 'corn', 'pasta', 'potato', 'rice', 'avocado', 'pancake', 'bread', 'broccoli', 'cheese', 'burrito', 'cereal', 'carrot', 'onion', 'apple', 'banana', 'sandwich', 'steak', 'burger', 'oatmeal', 'strawberry']  
    game_word = random.choice(foods_choice)
    print(str(len(game_word)) + " letters in the word")
  
  #Returns the word to the user but without showing the letters.
  return game_word
#---------------------------------------------------------------------------------------

"""
This section of code runs the hangman game, such as asking the user how many turns they
would like. It also asks the user for a letter, and it would then tell the user if the
letter is in the word or not. It also asks the user at the end if they would want to play again.
"""

def player_guess(game_word):
  
  #Asks the user how many turns they want.

  turn = int(input("\nHow many turns would you like? (Pick a number 1-20): "))
  ListNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  while turn not in ListNumbers:
    print('Please put a number. ')
    turn = int(input("\nHow many turns would you like? (Pick a number 1-20): "))

  # Asks the user to guess letter, documents weather it is right or wrong.
  # If wrong, takes away one turn. If right, aplies letter to the lines
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
      print("\n\n\033[1;32;40mCONGRATULATIONS, YOU WIN!")
      break
      
    guess = input(" Choose a Letter: ")

    while len(guess) != 1:
          print("only input one letter")
          guess = input(" Choose a letter: ")
  
 # Determines whether a guess was made correctly or incorrectly and deducts turns      
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
  # Asks player if they would like to play again
  single_again = input("\n\033[0;37;40mWould you like to play again?: ")
  while single_again != "yes" and "Yes" and "No" and "no":
    print("Only put yes or no.")
    single_again = input("\n\033[0;37;40mWould you like to play again?: ")
  
  # Determines the input of the user after asking to be played again
  if single_again == "Yes" or single_again == "yes":
    replit.clear()
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
      player()
  
  elif single_again == "No" or single_again == "no":
    print("\nNo problem, thanks for playing!")
  

#---------------------------------------------------------------------------------------
"""
This section of the code represents the introduction menu that allows the player to choose which game mode he would like to choose
"""

def menu():
  game_type = None
  tprint("HANGMAN", "Boxing")
  print("Welcome to Hangman! \n" )
  print("_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._")
  print("\n\nMenu-Options: \n\n [1]Single Player  [2]Multiplayer  ")
  try:
    game_type = int(input("\nWhat would you like to do?: "))
  except:
    print("Not an input.")
  
  
  replit.clear()
  return game_type
#---------------------------------------------------------------------------------------
'''This is the multiplayer code which allows for 2 players to compete one on one to see who can solve the word with the least amount of turns. '''

#Allows for the players to choose a category to play with.
def player():
  print("Welcome to multiplayer!")
  print("\nIn this mode, 2 players will go head to head in a 1v1 hang man battle.\n Player 1 will go first.")
    
  category = input("\nChoose a category from the following: Movies, Sports, Foods: ")

  #If the user enters an invalid input.
  while category != "movies" and category != "Movies"  and category!= "Sports" and category != "sports" and category != "Foods" and category != "foods":
    print("Not an input, try again.")
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

#Allows for the first player to begin guessing towards their word.
  player_1 = True
  while True:  
    if player_1 == True :
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
        
        #Asks the user for a letter input.
        guess = input(" Choose a letter: ")

        while len(guess) != 1:)
          print("Only input one letter")
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

# Begins the turn of player 2, and asks for their guesses to determine whether their input is in the word or not.

      print("Player 2 Turn.")
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

        while len(guess) != 1:
          print("on;y input one letter")
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
      player_1 = False
      break
          
      print("Player 2 Used " + str(10 - player_2_turn) + " Turns")
      
    # Determines the winner of the game or if it ended in a tie.

  if player_1_turn > player_2_turn:
    print("\n\033[1;32;40mPlayer 1 wins!")

  elif player_2_turn > player_1_turn:
    print("\n\033[1;32;40mPlayer 2 wins!")

  elif player_1_turn == player_2_turn :
    print("\033[1;32;40mIts a tie!")

  #Asks the user if they would like to play again.
  
  multi_again = input("\n\033[0;37;40mWould you like to play again?: ")
  
  if multi_again == "Yes" or multi_again == "yes":
    replit.clear()
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
      player()
  
  #If the user doesn't want to play again.
  elif multi_again == "No" or multi_again == "no":
    print("\nNo problem, thanks for playing!")


      
#---------------------------------------------------------------------------------------
"""
This code is designed to ensure the user picks a proper game type.
"""
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
  player()