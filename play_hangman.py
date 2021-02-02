from figure_hangman import lives
from features_hangman import Features

config = Features()

words_list = config.words()
guess_word = config.guess()
game_over = config.game_over()
tries = 6

game_name = """
\n===========================================================

\tH  A  N  G  M  A  N   :      T  H  E     G  A  M  E
\n===========================================================
"""
print(game_name)

result = []

for i in range(config.letter()):
    result += '_'

while not game_over:
    user_words = input('Guess the letters: ')

    if user_words in result:
        print(f'The guessed letter is {user_words}')

    for position in range(config.letter()):
        letter = guess_word[position]
        if letter == user_words:
            result[position] = letter

    if user_words not in guess_word:
        print(f'You guessed {user_words}. Incorrect letter. You lose a limb')
        tries -= 1
        if tries == 0:
            game_over = True
            print(f"The guess word is: '{guess_word}'")
            print('\nYou lose.\nBetter luck next time!')

    print(f"\n{' '.join(result)}")

    if '_' not in result:
        game_over = True
        print('You win. Congratulations!')

    print(lives[tries])
