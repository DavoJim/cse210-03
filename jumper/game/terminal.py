class Terminal:
    """Handles all terminal inputs/outputs."""

    def __init__(self):
        self._letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def guess_letter(self):
        """Asks the user to input a letter, validates and returns it

        Returns:
            The input letter
        """
        is_good_guess = False
        while is_good_guess == False:
            guess = input('Guess a letter: ').lower()
            if len(guess) == 0 :
                print("No guess submitted.")
            elif len(guess) > 1:
                print("You can only guess one letter at a time.")
            elif guess in self._letters: 
                is_good_guess = True
        
        return guess

    def write_outputs(self,*args):
        """Prints out all the arguments it is given
        
        Args:
            Any number of things that can be printed
        """
        for item in args:
            this_item = str(item)
            print(this_item)