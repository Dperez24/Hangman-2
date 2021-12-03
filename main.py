import random
"""
This code is for the game hangman, in which someone must guess
something from a category with a limited amount of guesses.
"""


#----------------------------------------------------------------------
def choose_word():
  category = input("Choose a category from the following: Movies, Sports, Foods: ")
    
  if category == "Movies" or category == "movies":
    movie_choice_list = [ 'starwars', 'joker', 'avatar', 'psycho', 'alien', 'scarface', 'inception', 'parasite', 'whiplash', 'gladiator', 'avengers']  
    word = random.choice(movie_choice_list)
  elif category == "Sports" or category == "sports":
    sports_choice_list = ['basketball', 'football', 'baseball']  
    word = random.choice(sports_choice_list)
  elif category == "Foods" or category == "foods":
    movie_choice_list = ['pizza', 'corn', 'pasta']  
    word = random.choice(movie_choice_list)
 

  return word

#----------------------------------------------------------------------
def player_guess(game_word):
  print("_" * len(game_word))
  turn = 12
  guesses = ""
  
  while turn > 0: 
    
    fails = 0
    for char in game_word:
      
      if char in guesses:
         print(char)
      else: 
        print("_") 
        fails = fails + 1
    
    if fails == 0:
      print("winner")
      break
      
    guess = input("Choose a letter: ")
    guesses += guess 
    if guess not in game_word:
      turn = turn - 1
      print("Wrong")
      print("turns left: " + str(turn))
        
      if turn == 0:
        print("you lose")
        break
  
    


game_word = choose_word()
player_guess(game_word)