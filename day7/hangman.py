import random

# import the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    lives_left_msg = f"****************************{lives}/6 LIVES LEFT****************************"
    print(lives_left_msg)
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed {guess}. Try another letter.")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter            
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"******************** The Word WAS {chosen_word}! YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # use the stages List from the file hangman_art.py
    print(stages[lives])
