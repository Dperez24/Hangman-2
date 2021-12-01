"""
This code is for the game hangman, in which someone must guess
something from a category with a limited amount of guesses.
"""
#----------------------------------------------------------------------
def choose_player():
  print("hi")

  
#----------------------------------------------------------------------
def choose_word():
  category = input("Choose a category from the following: Movies, Sports, Foods: ")
  
  if category == "Movies" or category == "movies":
    import random
    movie_choice_list = ['cinderella', 'star wars', 'avatar']  
    computer_movie_choice = random.choice(movie_choice_list)
    print(computer_movie_choice)
  elif category == "Sports" or category == "sports":
    import random
    sports_choice_list = ['basketball', 'football', 'baseball']  
    computer_sports_choice = random.choice(sports_choice_list)
    print(computer_sports_choice)
  if category == "Foods" or category == "foods":
    import random
    movie_choice_list = ['lotr', 'star wars', 'avatar']  
    computer_movie_choice = random.choice(movie_choice_list)
    print(computer_movie_choice)



#----------------------------------------------------------------------
def player_guess():
  print("hi")

choose_word()
