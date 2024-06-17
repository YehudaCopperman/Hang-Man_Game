# open screen
from random import randint
HANGMAN_ASCII_ART = """Welcom to Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/\n"""
                     
MAX_TRIES = randint(5, 10)


# main 
print(HANGMAN_ASCII_ART , MAX_TRIES , '\n')


# 7 posisions for the pole

print("""    x-------x
      
    x-------x
    |
    |
    |
    |
    |

    x-------x
    |       |
    |       0
    |
    |
    |
      
    x-------x
    |       |
    |       0
    |       |
    |
    |
    
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    | """)    

print('')
    
# guess a letter
guess = input("Guess a letter: ")

if guess.isalpha():
    if len(guess) == 1:
        guess = guess.lower()
        print(guess)
    else:
        print("E1")
elif len(guess) == 1:
    print("E2")
elif len(guess) > 1:
    print("E3")
else:
    print("You must enter a letter: ")
