# Create your Game class logic in here.
import random

from phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [' ',]

    def welcome(self):
        print('\n', '='*13, ' W E L C O M E   T O   P H R A S E H U N T E R ! ', '='*13, '\n')

    def create_phrases(self):

        all_phrases = [
            'Frankly my dear I dont give a damn', 
            'make him an offer he cant refuse', 
            'were not in Kansas anymore',
            'Heres looking at you kid',
            'Go ahead make my day',
            'May the force be with you',
            'You talkin to me',
            'I love the smell of napalm in the morning',
            'Theres no place like home',
            'Show me the money',
            'Youre gonna need a bigger boat',
            'ET phone home',
            'Ill have what shes having',
            'Hasta la vista baby',
            'Heres Johnny',
            'Take your stinking paws off me you damned dirty ape',
            'Elementary my dear Watson',
            'My mama always said life was like a box of chocolates',
            'Fear leads to anger anger leads to hate hate leads to suffering',
            'Bond James Bond',
            'Roads Where were going we dont need roads',
            'You cant handle the truth',
            'Ill be back',
            'If you build it he will come',
            'I feel the need the need for speed',
            'These arent the droids you’re looking for'
            'Choice is an illusion created between those with power and those without',
            'Carpe diem Seize the day',
            'Houston we have a problem',
            'Nobody puts baby in a corner',
            'Clever girl',
            'Do or do not there is no try',
            'Life uh finds a way',
            'Im king of the world']

        phrase_one = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_two = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_three = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_four = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))
        phrase_five = Phrase(all_phrases.pop(random.randint(0, len(all_phrases)-1)))

        phrases = [phrase_one, phrase_two, phrase_three, phrase_four, phrase_five]

        return phrases
    
    def get_random_phrase(self):
        rand = random.randint(0, len(self.phrases)-1)
        return self.phrases[rand]

    def get_guess(self):
        try:
            user_guess = input('Take a guess, any letter will do!\n>').lower()
            accepted_values =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            if user_guess not in accepted_values:
                raise ValueError('Please enter a single letter from a-z')
            else:
                return user_guess
        except ValueError as err:
            print(f'There was an error. {err}')
        except TypeError:
            print(f'There was an error.')

    def start(self):
        self.welcome()
        
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f'Number Missed: {self.missed}')
            self.active_phrase.display(self.guesses)

            user_guess = self.get_guess()
            self.guesses.append(user_guess)

            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        
        self.game_over()
            
    
    def game_over(self):
        if self.missed == 5:
            print('='*13, 'GAME OVER!', '='*13)
        elif self.active_phrase.check_complete(self.guesses):
            print('='*13, 'YAHOOOO! You Got it!', '='*13) 
            self.active_phrase.display(self.guesses)