import random
import csv

class Word():
    """Choose a random word, break it into letters, and compare our guesses.

        Attributes:
        _letters []: the word that's being guessed, broken up into a list of letters, guesses
        _guesses []: letters that have been guessed

    """

    def __init__(self, word_str:str=""):
        """Constructs a new Word
            Args:
                self: an instance of Word
                word_str: optionally, for debugging, can choose the word
        """
        if word_str == "":
            self._word = self._choose().lower()
        else:
            self._word = word_str.lower()
        self._guesses = []
        self._letters = []
        for letter in self._word:
            if letter not in self._letters:
                self._letters.append(letter.lower())
        
    def _choose(self):
        """Chooses a random new word out of a list of words
            Returns: the random word
        """
        with open(r"jumper/game/word_list.csv") as word:
            reader = csv.reader(word)
            next(reader)
            return random.choice(list(reader))[0]
        
        
    
    def guess(self,guess:str):
        """ Takes a guess, checks if it is in the letters list and adds it to the guesses
            Args:
                guess: a letter from the player
            Returns: 
                a boolean which indicates whether the guess was in the word or not
        """
        guess = guess.lower()
        self._guesses.append(guess)
        return guess.lower() in self._letters

    def __str__(self):
        output = ''
        for letter in self._word:
            if letter in self._guesses:
                output += letter.upper()
            else:
                output += '_'
            output += ' '
        return output
    
    def getGuesses(self):
        if len(self._guesses) == 0:
            return 'None'
        return ''.join(self._guesses)
    
    def getWord(self):
        return self._word

if __name__ == "__main__":
    word = Word()
    print(word._word)
    word.guess('P')
    print(word.guess('q'))
    print(word)

    