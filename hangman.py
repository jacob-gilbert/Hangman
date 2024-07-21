import random

words = ['python', 'anaconda', 'garter', 'cobra', 'mamba']
used_letters = set()

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
if gamemode == "1":
    # randomly choose a word from the list
    chosen_word = random.choice(words)
    word_display = ['_' for _ in chosen_word]
    attempts = 8 # number of allowed attempts
else:
    # player inputs word and number of attempts they want to allow another player
    chosen_word = input("Type your word:\n")
    for i in range(15):
        print()
    word_display = ['_' for _ in chosen_word]
    while True:
        attempts = input("How many attempts would you like to give the other player (must be between 5 and 12)?\n")
        if attempts in ['5', '6', '7', '8', '9', '10', '11', '12']:
            break
        print("Number must be between 5 and 12, try again")
    attempts = int(attempts)

while attempts > 0 and '_' in word_display:
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
        if attempts == 0:
            print("0 Mistakes Left, You Failed")
        else:
            print("Mistakes Left:", attempts)
    
# when the game ends
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))