import Tkinter
import string
import random

window = Tkinter.Tk()
window.title("Hangman, The word Game!")
window.geometry("400x540")
r = Tkinter.Label(window, text="Hello, Gaurav Verma !!\n______________________________________________\nRULES OF THE GAME:",bg="snow")
r.pack()
rules = Tkinter.Message(window, text="The computer will guess a random word and It will let you know the number of letters in it. You have to guess the word by entering One Letter at a time.If the guessed letter is correct, all occurrences of that particular letter will be revealed. If your guess is wrong, there will be a decreament in the remaining guesses. You will be provided with eight initial guesses. Enjoy! ")
rules.pack() 
sugg = Tkinter.Label(window, text = "Suggestions should be mailed at galileo.verma@gmail.com.")
sugg.pack(side = "bottom")


WORDLIST_FILENAME = "words.txt" 



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    #welcome = Tkinter.Label(window, text="Welcome to the Hangman game!")
    #welcome.pack()
    #loading = Tkinter.Label(window, text="Loading word list from file...")
    #loading.pack()
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #string1 =  "  " + str(len(wordlist))  + " words loaded."
    #num = Tkinter.Label(window, text=string1)
    #num.pack()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    verifier = 0
    for char in secretWord:
        for char2 in lettersGuessed:
            if char == char2:
                verifier = 1
                break
            else:
                verifier = 0
        if verifier == 0:
            return False
    return True




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordShow = ''
    verifier = 0
    for char in secretWord:
        for char2 in lettersGuessed:
            if char == char2:
                verifier = 1
                break
            else:
                verifier = 0
        if verifier == 0:
            if wordShow != '' and wordShow[-1] == '_':
                wordShow = wordShow + ' _'
            else:
                wordShow = wordShow + '_'
        if verifier == 1:
            wordShow = wordShow + char
    return wordShow




def getAvailableLetters(lettersGuessed):
    verifier = 0
    word = ''
    for char in string.ascii_lowercase:
        for char2 in lettersGuessed:
             if char == char2:
                 verifier = 1
                 break
             else:
                 verifier = 0 
        if verifier == 0:
            word = word + char
    return word
    
   
def guessInLower(guess):
    if guess >= 'A' and guess <= 'Z':
        return guess.lower()
    else:
        return guess   


def verify_and_update(guess):
    def newGame():
        clear_old()
        global welcome
        global loading
        global num
        global length
        welcome.destroy()
        loading.destroy()
        num.destroy()
        length.destroy()
        result.destroy()
        secret_word.destroy()
        as_fornewgame.destroy()
        new_game.destroy()
        global wordlist
        global secretWord
        global guesses_left
        global stringer
        global lettersGuessed
        global rev_word
        global please
        global guess_entry
        global submit
        global theguesses_left
        global hell
        global msg
        global guess
        wordlist = loadWords()
        secretWord = chooseWord(wordlist)
        stringer = ""
        hell=""  
        guess = ""  
        guesses_left = 8
        lettersGuessed = ""
        welcome = Tkinter.Label(window, text="_________________________________________\nWelcome to the Hangman game!")
        welcome.pack()
        loading = Tkinter.Label(window, text="Loading word list from file...")
        loading.pack()
        string1 =  "  " + str(len(wordlist))  + " words loaded."
        num = Tkinter.Label(window, text=string1)
        num.pack()
            
        #This does not have to be changed
        string2 = "I am thinking of a word that is "+ str(len(secretWord)) + " letters long.\n_________________________________________\n"
        length = Tkinter.Label(window, text=string2)
        length.pack()
        
        #This has to be cleared and updated after verifying the status of guess, each time
        for char in secretWord:
                stringer = stringer + " _"
        rev_word = Tkinter.Label(window, text = stringer)
        rev_word.pack()
        
        #This is the entry field...It might have to be deleted and created.
        please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
        please.pack()
        
        hell = Tkinter.StringVar()
        hell.set("")
        guess_entry = Tkinter.Entry(window,textvariable=hell)
        guess_entry.pack()
        guess_entry.focus_set()
        submit = Tkinter.Button(window,text="Submit guess", command=feedin)
        submit.pack()
        
        #This has to be continuously updated after each hit
        #Initially it has to be 8 guesses left
        theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
        theguesses_left.pack()
        
        msg = Tkinter.Label(window, text="") 
        msg.pack()
        return
    crap = 0
    global guesses_left
    global stringer
    global lettersGuessed
    global rev_word
    global please
    global guess_entry
    global submit
    global theguesses_left
    global hell
    global msg
    global result
    global secret_word
    global new_game
    stringer =""
    if len(guess) > 1 or guess == "":
        #This has to be cleared and updated after verifying the status of guess, each time
        clear_old()
        stringer = getGuessedWord(secretWord, lettersGuessed)
        rev_word = Tkinter.Label(window, text = stringer)
        rev_word.pack()
        
        #This is the entry field...It might have to be deleted and created.
        please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
        please.pack()
        
        hell = Tkinter.StringVar()
        hell.set("")
        guess_entry = Tkinter.Entry(window,textvariable=hell)
        guess_entry.pack()
        guess_entry.focus_set()
        submit = Tkinter.Button(window,text="Submit guess", command=feedin)
        submit.pack()
        msg = Tkinter.Label(window, text="ERROR: Please enter ONE LETTER at a time.") 
        msg.pack()
        #This has to be continuously updated after each hit
        #Initially it has to be 8 guesses left
        theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
        theguesses_left.pack()
        return
    for var in lettersGuessed:
        if guess == var:
            clear_old()
            stringer = getGuessedWord(secretWord, lettersGuessed)
            rev_word = Tkinter.Label(window, text = stringer)
            rev_word = Tkinter.Label(window, text = stringer )
            rev_word.pack()
            
            #This is the entry field...It might have to be deleted and created.
            please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
            please.pack()
            
            hell = Tkinter.StringVar()
            hell.set("")
            guess_entry = Tkinter.Entry(window,textvariable=hell)
            guess_entry.pack()
            guess_entry.focus_set()
            submit = Tkinter.Button(window,text="Submit guess", command=feedin)
            submit.pack()
            
            #This has to be continuously updated after each hit
            #Initially it has to be 8 guesses left
            theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
            theguesses_left.pack()
            msg = Tkinter.Label(window, text="You have already entered that letter.") 
            msg.pack()
            return
    lettersGuessed = lettersGuessed + guess
    for let in secretWord:
        if guess == let:
            clear_old()
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                result = Tkinter.Label(window, text ="Congrats!\nYou guessed the word correctly! You Won!")
                result.pack()
                secret_word = Tkinter.Label(window, text="The word, as you correctly guessed, was " + secretWord + "\n_________________________________________")
                secret_word.pack()
                as_fornewgame = Tkinter.Label(window, text = "Click the button to start a new game.")
                as_fornewgame.pack()
                new_game = Tkinter.Button(window, text="New Game!", command=newGame)
                new_game.pack()
                return
            stringer = getGuessedWord(secretWord, lettersGuessed)
            rev_word = Tkinter.Label(window, text = stringer )
            rev_word.pack()
            please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
            please.pack()
            hell = Tkinter.StringVar()
            hell.set("")
            guess_entry = Tkinter.Entry(window,textvariable=hell)
            guess_entry.pack()
            guess_entry.focus_set()
            submit = Tkinter.Button(window,text="Submit guess", command=feedin)
            submit.pack()
            theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
            theguesses_left.pack()
            msg = Tkinter.Label(window, text="That was a good guess!") 
            msg.pack()
            crap = 1
            break
    if crap != 1:
        clear_old()
        guesses_left = guesses_left - 1
        if guesses_left == 0 and getGuessedWord(secretWord, lettersGuessed) != secretWord:
            clear_old()
            result = Tkinter.Label(window, text ="Oops!\nYou ran out of guesses! You have lost the game.")
            result.pack()
            secret_word = Tkinter.Label(window, text = "The word was "+ secretWord + "\n_________________________________________")
            secret_word.pack()
            as_fornewgame = Tkinter.Label(window, text = "Click the button to start a new game.")
            as_fornewgame.pack()
            new_game = Tkinter.Button(window, text="New Game!", command=newGame)
            new_game.pack()
            return 
        stringer = getGuessedWord(secretWord, lettersGuessed)
        rev_word = Tkinter.Label(window, text = stringer )
        rev_word.pack()
        please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
        please.pack()
        hell = Tkinter.StringVar()
        hell.set("")
        guess_entry = Tkinter.Entry(window,textvariable=hell)
        guess_entry.pack()
        guess_entry.focus_set()
        submit = Tkinter.Button(window,text="Submit guess", command=feedin)
        submit.pack()
        
        theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
        theguesses_left.pack()
        msg = Tkinter.Label(window, text="Wrong guess.") 
        msg.pack()
        return         
           
    return

def clear_old():
    rev_word.destroy()
    please.destroy()
    guess_entry.destroy()
    submit.destroy()
    theguesses_left.destroy()
    msg.destroy()
    return


def finish():
    window.destroy()
    return

def feedin():
    global guess
    guess = hell.get()
    guess = guessInLower(guess)
    clear_old()
    verify_and_update(guess)
    #print guess
    return


wordlist = loadWords()
secretWord = chooseWord(wordlist)



stringer = ""
hell=""  
guess = ""  
guesses_left = 8
lettersGuessed = ""
welcome = Tkinter.Label(window, text="_________________________________________\nWelcome to the Hangman game!")
welcome.pack()
loading = Tkinter.Label(window, text="Loading word list from file...")
loading.pack()
string1 =  "  " + str(len(wordlist))  + " words loaded."
num = Tkinter.Label(window, text=string1)
num.pack()

#This does not have to be changed
string2 = "I am thinking of a word that is "+ str(len(secretWord)) + " letters long.\n_________________________________________\n"
length = Tkinter.Label(window, text=string2)
length.pack()

#This has to be cleared and updated after verifying the status of guess, each time
for char in secretWord:
        stringer = stringer + " _"
rev_word = Tkinter.Label(window, text = stringer)
rev_word.pack()

#This is the entry field...It might have to be deleted and created.
please = Tkinter.Label(window, text = "Please enter your guess below and press the 'Submit' button.")
please.pack()

hell = Tkinter.StringVar()
hell.set("")
guess_entry = Tkinter.Entry(window,textvariable=hell)
guess_entry.pack()
guess_entry.focus_set()
submit = Tkinter.Button(window,text="Submit guess", command=feedin)
submit.pack()

#Initially it has to be 8 guesses left
theguesses_left = Tkinter.Label(window, text="You have " + str(guesses_left) + " guesses left.")
theguesses_left.pack()

msg = Tkinter.Label(window, text="") 
msg.pack()

finish = Tkinter.Button(window, text="Exit Game", command=finish)
finish.pack(side="bottom")
window.mainloop()
