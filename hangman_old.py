import random

# number of players / one person picks a word or the computer picks a word
def players_selection():
    num_players = 0
    print("Select your gamemode:")
    while True:
        num_players = input("If you want the computer to choose a word press 1\nor if you want to choose a word press 2\n")
        if num_players == "1" or num_players == "2":
            break
    return num_players

gamemode = players_selection()
if gamemode == "2":
    player1 = input("\nSubmit a name for player 1, this person chooses the word first\n")
    player2 = input("Submit a name for player 2, this person guesses the word first\n")
num_games = 1
won1 = 0
won2 = 0
print("\nThis is game", num_games)
# the above lines are outside the while loop because this information
# either stays constant the entire time or is incremented in the while loop

# the below while loop gives the ability to play multiple games without rerunning the program
# if the players no long wish to continue the while loop will break and the program will stop
while True:
    words = ['python', 'anaconda', 'garter', 'cobra', 'mamba']
    used_letters = set()

    # single player
    if gamemode == "1":
        # randomly choose a word from the list
        chosen_word = random.choice(words)
        word_display = ['_' for _ in chosen_word]
        attempts = 8 # number of allowed attempts

    # 2 players
    else:
        # player inputs word and number of attempts they want to allow another player
        chosen_word = input("Type your word:\n")
        # hides the choosen word by print multiple blank lines so the guessing player cannot see it
        for i in range(15):
            print()
        word_display = ['_' for _ in chosen_word]

        # forces uses to pick between allowing 5 guesses to 12 guesses, breaks once a number is chosen that is in this range
        while True:
            attempts = input("How many attempts would you like to give the other player (must be between 5 and 12)?\n")
            if attempts in ['5', '6', '7', '8', '9', '10', '11', '12']:
                break
            print("Number must be between 5 and 12, try again")
            
        # input is automatically made as a string, so convert to int to process it as a number
        attempts = int(attempts)

    # while loop breaks if you player runs out of attempts or correctly guesses the word
    while attempts > 0 and '_' in word_display:

        # shows the player which letters have been guessed correctly and where they are in the word
        print('\n' + ' '.join(word_display))
        print("Mistakes Left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in used_letters:
            print(f"{guess} already guessed, choose a new letter")
        elif guess in chosen_word:
            used_letters.add(guess)
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess # reveal letter(s)
        else:
            print(f"{guess} does not appear in the word")
            used_letters.add(guess)
            attempts -= 1

            # prints winner when someone has run out of attempts
            if attempts == 0:
                print("0 Mistakes Left, You Failed")
                if gamemode == "2":
                    if num_games % 2 == 0:
                        print(player2, "won!")
                        won2 += 1
                    else:
                        print(player1, "won!")
                        won1 += 1
            else:
                print("Mistakes Left:", attempts)
        
    # when the game ends from correctly guessing the word
    if '_' not in word_display:
        print("You guessed the word!")
        print(' '.join(word_display))
        if gamemode == "2":
            if num_games % 2 == 1:
                print(player2, "won!")
                won2 += 1
            else:
                print(player1, "won!")
                won1 += 1
    
    print("\nGame", num_games, "over!")

    # shows updated scoreboard
    if gamemode == "2":
        print(f"Scoreboard: {player1} won {won1} games and {player2} won {won2} games so far")
    
    play_again = input("Would you like to play again (y/n)?\n")
    num_games += 1
    if play_again != 'y':
        break
    if gamemode == "2":
        print("\nSwitch who chooses the word and who guesses the word")