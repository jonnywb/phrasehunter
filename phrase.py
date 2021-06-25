class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    # Displays either the letter or an underscore (with added spaces) 
    # ...depending on the content of 'guesses' list
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end=' ')
            else: 
                print(f'_', end=' ')
        
        print('\n')
    
    # Check if letter guessed was correct
    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False
    
    # Check if word has been guessed correctly
    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
