import random

from phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ', ',', '.', '!', '?', '\'']

    def welcome(self):
        print('\n', '='*13, ' W E L C O M E   T O   P H R A S E H U N T E R ! ', '='*13, '\n')

    def create_phrases(self):
        all_phrases = [
            'Frankly my dear, I don\'t give a damn.', 
            'make him an offer he can\'t refuse.', 
            'we\'re not in Kansas anymore.',
            'Here\'s looking at you, kid.',
            'Go ahead, make my day.',
            'May the force be with you',
            'You talkin\' to me?',
            'I love the smell of napalm in the morning.',
            'There\'s no place like home.',
            'Show me the money!',
            'You\'re gonna need a bigger boat.',
            'E.T. phone home',
            'I\'ll have what she\'s having.',
            'Hasta la vista, baby.',
            'Here\'s Johnny!',
            'Take your stinking paws off me, you damned dirty ape!',
            'Elementary, my dear Watson.',
            'My mama always said, life was like a box of chocolates.',
            'Fear leads to anger, anger leads to hate, hate leads to suffering.',
            'Bond, James Bond',
            'Roads? Where we\'re going, we don\'t need roads.',
            'You can\'t handle the truth!',
            'I\'ll be back.',
            'If you build it, he will come.',
            'I feel the need, the need for speed!',
            'These aren\'t the droids you\'re looking for.',
            'Choice is an illusion, created between those with power, and those without.',
            'Carpe diem. Seize the day!',
            'Houston, we have a problem.',
            'Nobody puts baby in a corner!',
            'Clever girl.',
            'Do or do not, there is no try.',
            'Life uh... finds a way.',
            'I\'m king of the world!']

        # Each variable removes and stores a random phrase from the list
        phrase_one = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_two = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_three = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_four = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_five = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))

        phrases = [phrase_one, phrase_two, phrase_three, phrase_four, phrase_five]

        return phrases
    
    # Pick one random phrase from the five available choices in self.phrases
    def get_random_phrase(self):
        rand = random.randint(0, len(self.phrases)-1)
        return self.phrases[rand]

    # User input method
    def get_guess(self):
        # While loop to allow for errors
        while True:
            try:
                user_guess = input('Take a guess, any letter will do!\n>').lower()
                accepted_values =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                if user_guess.lower() in accepted_values:
                    print(user_guess)
                    return user_guess
                else:
                    raise TypeError('Please enter a single letter between a-z.')

            except TypeError as err:
                print(f'Error: {err}')

    # Start Game
    def start(self):
        self.welcome()
        
        # Loop until either player loses their five lives, or finishes the phrase.
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            lives_remaining = 5 - self.missed
            print(f'\nYou have {lives_remaining} out of 5 lives remaning.\n')
            self.active_phrase.display(self.guesses)

            user_guess = self.get_guess()
            self.guesses.append(user_guess)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        
        self.game_over()
            
    # Game over checks whether the game was ended due to win or loss
    # and displays relevent message.
    def game_over(self):
        if self.missed == 5:
            print('='*13, 'G A M E   O V E R !', '='*13, '\n')
        elif self.active_phrase.check_complete(self.guesses):
            print('='*13, 'C O N G R A T U L A T I O N S ! You Got it!', '='*13, '\n') 
            self.active_phrase.display(self.guesses)
        
        self.play_again()

    # When called, asks user if they would like to play again.
    # Y = Resets code and calls start.game() again.
    # N = Quits the game and displays a message
    # Else Error.
    def play_again(self):

        print('Would you like to play again?')
        while True:
            try:
                answer = input('Please enter \'y\' or \'n\'. \n>')

                if answer.lower() != 'y' and answer.lower() != 'n':
                    raise ValueError('Please enter \'y\' or \'n\'.')

                elif answer == 'y':
                    # RESET
                    self.phrases = self.create_phrases()
                    self.active_phrase = self.get_random_phrase()
                    self.missed = 0
                    self.guesses = [' ', ',', '.', '!', '?', '\'']
                    self.start()

                elif answer == 'n':
                    print('\nThanks for playing!\n')
                    break

            except ValueError as err:
                print(f'Please try again. {err}')
