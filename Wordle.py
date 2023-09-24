# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter
from WordleDictionary import ENGLISH_WORDS, ITALIAN_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

DICTIONARY = []

def wordle():
    rows = N_ROWS
    cols = N_COLS
    guess = 0
    win = False
    # wordToGuess = random.choice(FIVE_LETTER_WORDS)
    wordToGuess = ''
    tempList = wordToGuess
    lettersUsed = []
    print(wordToGuess)

# def lang_switch b
#  
    def enter_action(s):
        print(s)
        if gw._lang == "English":
            DICTIONARY = ENGLISH_WORDS
            wordToGuess = random.choice(DICTIONARY)
        else: 
            DICTIONARY = ITALIAN_WORDS
            wordToGuess = random.choice(DICTIONARY)
            if s.lower() in DICTIONARY:
                gw.show_message("Real word")
                for n in range(0,len(wordToGuess)):
                    letterGuess = gw.get_square_letter(gw.get_current_row(),n).lower()
                    
                    if letterGuess == wordToGuess[n]:
                        gw.set_square_color(gw.get_current_row(),n,CORRECT_COLOR)
                        lettersUsed.append(letterGuess)
                    elif letterGuess in tempList:
                        if letterGuess not in lettersUsed :
                            gw.set_square_color(gw.get_current_row(), n, PRESENT_COLOR)
                        lettersUsed.append(letterGuess)
                    else:
                        gw.set_square_color(gw.get_current_row(), n, MISSING_COLOR)
                        lettersUsed.append(letterGuess)
                
                if s.lower() == wordToGuess:
                    gw.show_message("Congrats! Winner in " + str(gw.get_current_row()+1) + "!!!")
                else:
                    gw.set_current_row(gw.get_current_row() + 1)
            else:
                gw.show_message("Not a real word")
        
        print(gw.get_current_row())
        return

    gw = WordleGWindow()
    print(wordToGuess)

    gw.add_enter_listener(enter_action)

    # for n in (range(0, len(wordToGuess))):
    #     gw.set_square_letter(gw.get_current_row(), n, wordToGuess[n])
# Startup code

if __name__ == "__main__":
    wordle()
    

