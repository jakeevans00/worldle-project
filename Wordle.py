# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR


def wordle():
    # wordToGuess = random.choice(FIVE_LETTER_WORDS)
    wordToGuess = "ruder"
    tempList = wordToGuess
    lettersUsed = []
    print(wordToGuess)

    def enter_action(s):
        print(s)
        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Real word")

            for n in range(0, len(wordToGuess)):
                letterGuess = gw.get_square_letter(gw.get_current_row(), n).lower()

                if letterGuess == wordToGuess[n]:
                    gw.set_square_color(gw.get_current_row(), n, CORRECT_COLOR)
                    gw.set_key_color(letterGuess.upper(), CORRECT_COLOR)
                    lettersUsed.append(letterGuess)
                elif letterGuess in tempList:
                    if letterGuess not in lettersUsed:
                        gw.set_square_color(gw.get_current_row(), n, PRESENT_COLOR)
                        if gw.get_key_color(letterGuess.upper()) == CORRECT_COLOR:
                            continue
                        else:
                            gw.set_key_color(letterGuess.upper(), PRESENT_COLOR)
                    else:
                        gw.set_square_color(gw.get_current_row(), n, MISSING_COLOR)
                        if gw.get_key_color(letterGuess.upper()) == CORRECT_COLOR:
                            continue
                        else:
                            gw.set_key_color(letterGuess.upper(), MISSING_COLOR)
                    lettersUsed.append(letterGuess)
                else:
                    gw.set_square_color(gw.get_current_row(), n, MISSING_COLOR)
                    gw.set_key_color(letterGuess.upper(), MISSING_COLOR)
                    lettersUsed.append(letterGuess)

            if s.lower() == wordToGuess:
                gw.show_message(
                    "Congrats! Winner in " + str(gw.get_current_row() + 1) + "!!!"
                )
            else:
                gw.set_current_row(gw.get_current_row() + 1)
                lettersUsed.clear()
        else:
            gw.show_message("Not a real word")

        print(gw.get_current_row())
        return

    gw = WordleGWindow()

    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
