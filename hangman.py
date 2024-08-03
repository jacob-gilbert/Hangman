import tkinter
import random
import string

WORD_LIST = ["ABANDONMENT", "ACCEPTANCE", "BACKWARDNESS", "BLACKSMITH", "CALCULATE", "CHALLENGE",
    "CLASSROOM", "CONTRACTOR", "DIFFICULT", "DIFFERENT", "DISCOVERY", "EDUCATION",
    "EMPHASIS", "ENGINEER", "EXPERIENCE", "FOREVER", "GENERATOR", "IMAGINE", "INCREDIBLE",
    "INSTITUTE", "JOURNALISM", "LABORATORY", "LEARNING", "LEGITIMATE", "LITERATURE", 
    "MYSTERIOUS", "OBLIGATION", "OPERATION", "PARLIAMENT", "PERFORMANCE", "PRESENTATION",
    "PROFOUND", "QUESTION", "RECOVERY", "RECRUITMENT", "RESILIENCE", "ROMANTIC", "SCIENTIFIC",
    "SITUATION", "SOLUTION", "STRENGTHEN", "STRUCTURE", "SUDDENLY", "TECHNOLOGY", "UNIVERSAL",
    "VOCABULARY", "VOLUNTEER", "WILDERNESS", "ADVENTURE", "AFTERSHOCK", "BEAUTIFUL", "BRILLIANCE",
    "CALCULATION", "CAMPAIGN", "COMPLICATED", "COUNTRYSIDE", "CUSTOMER", "DICTIONARY", "DOMINANCE",
    "ESTABLISHMENT", "EXCELLENCE", "FANTASTIC", "FASHIONABLE", "FREELANCE", "GENEROSITY", "HORIZON",
    "IDENTICAL", "IMPORTANT", "INCREDIBLE", "INSTITUTE", "INSISTENCE", "INVENTION", "JOURNALIST",
    "LOCATION", "LUMINOUS", "MAINTENANCE", "MARVELLOUS", "METROPOLITAN", "OPERATION", "OPPONENT",
    "PERCEPTION", "PHOTOGRAPH", "PREPARATION", "PROTECTION", "RATIONAL", "RELIABLE", "REPUTATION",
    "SIGNIFICANT", "STRATEGIC", "SUPERIOR", "TECHNOLOGY", "TRADITION", "TRANQUILITY", "UNFORTUNATE",
    "UNIVERSAL", "VARIETY", "VOCATION", "WONDERFUL", "WORSHIP", "ABSTRACTION", "ATTRACTIVE",
    "COLLECTION", "CONCLUSION", "DESTINATION", "DYNAMICALLY", "ENVIRONMENT", "EXPRESSION",
    "GATHERING", "INSPIRATION", "KNOWLEDGE", "LUXURIOUS", "METAPHORICAL", "PARTICULAR", "PROFESSIONAL",
    "REMARKABLE", "SENSATIONAL", "TRANSPORTATION", "UNBELIEVABLE"]

ROWS = 15
COLS = 15
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def new_game():
    global word, guesses, word_length, gameover, won, known_letters_list, known_letters_string, known_letters, clicked_set

    new_word = WORD_LIST[random.randint(0, len(WORD_LIST)-1)]
    while (new_word == word):
        new_word = WORD_LIST[random.randint(0, len(WORD_LIST)-1)]
    word = new_word

    guesses = 7
    word_length = len(word)
    gameover = False
    won = False
    known_letters_list = ["_"] * word_length
    known_letters_string = "_ " * word_length
    known_letters = 0
    clicked_set = set()

    # reset the letters
    for index, letter in enumerate(alphabet):
        row = index // num_columns  # Calculate row based on index
        column = index % num_columns  # Calculate column based on index
        button = tkinter.Button(frame_right, text=letter, font=("Consolas"))
        button.grid(row=row, column=column, padx=10, pady=10, sticky='ew')

        # Bind the button click event to the function
        button.config(command=lambda b=button: on_button_click(b))

    # reset the known letters visible on the screen
    letters_to_guess.config(text=known_letters_string)

def on_button_click(button):
    global known_letters_list, known_letters_string, known_letters, won

    # if the game is over don't want the user's clicks to change any of the letters
    if (gameover or won):
        return
    
    letter = button.cget('text')  # Get the button's text

    if letter in clicked_set:
        return
    else:
        clicked_set.add(letter)

    if letter in word:
        button.config(bg='green')
        update_guesses(True)
        
        count = 0
        for char in word:
            if char == letter:
                known_letters_list[count] = letter
                known_letters += 1
            count += 1
        
        known_letters_string = ""
        for _ in known_letters_list:
            known_letters_string = known_letters_string + _ + " "
        letters_to_guess.config(text=known_letters_string)

        if known_letters == word_length:
            won = True
    else:
        button.config(bg='red')
        update_guesses(False)


def draw():
    global guesses

    canvas.delete("all")
    
    if (gameover):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20",
                           text=f"Game Over", fill="red")
    elif (won):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font="Arial 20",
                           text=f"You Won!", fill="red")
    else:
        canvas.create_text(60, 20, font="Arial 10", text=f"Guesses Left: {guesses}", fill="black")

    window.after(100, draw) # after 100ms we call draw again which is 10 frames/sec


def update_guesses(right):
    global guesses, gameover

    if (not right):
        guesses -= 1
        if guesses == 0:
            gameover = True


# initialize game
word = WORD_LIST[random.randint(0, len(WORD_LIST)-1)]
guesses = 7
word_length = len(word)
gameover = False
won = False
known_letters_list = ["_"] * word_length
known_letters_string = "_ " * word_length
known_letters = 0
clicked_set = set()

# game window
window = tkinter.Tk()
window.title("Hangman")
window.resizable(False, False) # user cannot change the size of the window

frame_left = tkinter.Frame(window, bg='lightblue')
frame_left.grid(row=0, column=0, sticky='nsew')

canvas = tkinter.Canvas(frame_left, bg="white", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)

frame_right = tkinter.Frame(window, bg="lightgray")
frame_right.grid(row=0, column=1, sticky='nsew')

# Add alphabet buttons to the right frame
alphabet = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Number of columns for buttons
num_columns = 7

for index, letter in enumerate(alphabet):
    row = index // num_columns  # Calculate row based on index
    column = index % num_columns  # Calculate column based on index
    button = tkinter.Button(frame_right, text=letter, font=("Consolas"))
    button.grid(row=row, column=column, padx=12, pady=10, sticky='ew')

    # Bind the button click event to the function
    button.config(command=lambda b=button: on_button_click(b)) # the last assignment of button is Z, so if we do not set b = button and just use button it will only be Z, b = button remembers the specific letter when each iteration of the for loop runs

# creating a restart button
restart_button = tkinter.Button(frame_right, text="New Game", font=("Consolas"), background="red",
                        foreground="white", command=new_game)
restart_button.grid(row=6, column=0, columnspan=2, sticky="nsew")

frame_below = tkinter.Frame(window, bg="navy")
frame_below.grid(row=1, column=0, columnspan=2, sticky="nsew")

# creating a label to display the known and unknown letters of the word to be guessed
letters_to_guess = tkinter.Label(frame_below, text=known_letters_string , font=("Consolas", 40),
                      background="navy", foreground="white")
letters_to_guess.pack(fill = "x")

window.update()

# center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() - 75 # the -75 is specific to my screen

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


draw()

window.mainloop()