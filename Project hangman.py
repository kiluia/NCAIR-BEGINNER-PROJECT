import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = ""
        self.word_length = 0
        self.ai_guesses=set()
        self.user_guesses= set()
        self.max_attempts = 6
        self.option = 0
        
    def start_game(self):
        self.secret_word = random.choice(self.word_list).lower()
        self.word_length = len(self.secret_word)
        self.user_guesses = set()
        self.ai_guesses=set()

    def make_user_guess(self):
        while True:
            guess = input("Your guess: ").lower()
            if guess.isalpha() and len(guess) == 1 and guess not in self.user_guesses:
                break
            else:
                print("Invalid guess. Please enter a single letter you haven't guessed before.")
        self.user_guesses.add(guess)
        return guess

    def make_ai_guess(self):
        available_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in self.ai_guesses]
        guess = random.choice(available_letters)
        self.ai_guesses.add(guess)
        return guess
    
    def display_word_state(self,guesses):
        return ''.join([letter if letter in guesses else '_' for letter in self.secret_word])

    def play_game(self):
        print("Welcome to Hangman!")
        self.start_game()

        while True:
            
            # User's turn
            print("\nPlayer One's Current State:", self.display_word_state(self.user_guesses))
            user_guess = self.make_user_guess()
            if user_guess in self.secret_word:
                print("Correct guess!")
            else:
                print("Incorrect guess.")
                self.max_attempts -= 1

            if '_' not in self.display_word_state(self.user_guesses):
                print("Congratulations! You guessed the word:", self.secret_word)
                break

            if self.max_attempts == 0:
                print("Out of attempts.")
            
            ai_guess = self.make_ai_guess()
            print("\nPlay Two's Current State:", self.display_word_state(self.ai_guesses))
            print("\nAI's turn:",ai_guess)
            # AI's turn
            if ai_guess in self.secret_word:
                print("AI's Correct guess!")
            else:
                print("AI's Incorrect guess.")
                self.max_attempts -= 1

            if '_' not in self.display_word_state(self.ai_guesses):
                print("Congratulations! AI guessed the word:", self.secret_word)
                break

            if self.max_attempts == 0:
                print("Out of attempts. The correct word was:", self.secret_word)
                break
    
    def single(self):
            self.start_game()
            while self.max_attempts > 0:
                print("\nPlayer One's Current State:", self.display_word_state(self.user_guesses))
                user_guess = self.make_user_guess()
                if user_guess in self.secret_word:
                    print("Correct guess!")
                else:
                    print("Incorrect guess.")
                    self.max_attempts -= 1

                if '_' not in self.display_word_state(self.user_guesses):
                    print("Congratulations! You guessed the word:", self.secret_word)
                    break
                if self.max_attempts == 0:
                    print("Out of attempts. \n GAME OVER!!!")
    def begin(self):
        print("WELCOME TO HANGMAN")
        print("Select the game you want to play")
        print("1. Single Player")
        print("2.Play with Computer\n")
        self.option = int(input())
        if self.option==1:
            return self.single()
        elif self.option==2:
            return self.play_game()
        else:
            print('Incorrect input try again')
            return self.begin()
        

# Example usage
word_list = ["hangman", "python", "computer", "programming", "algorithm", "huggingface"]
hangman_game = HangmanGame(word_list)
hangman_game.begin()