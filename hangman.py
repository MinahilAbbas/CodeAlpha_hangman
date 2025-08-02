import random

word_list = ["banana", "orange", "monkey", "dubai", "sirilanka"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def play_game():
    word_to_guess = random.choice(word_list)
    word_to_display = ['_'] * len(word_to_guess)

    # Reveal 1 or 2 letters randomly
    num_to_reveal = random.randint(1, 2)
    revealed_indexes = random.sample(range(len(word_to_guess)), num_to_reveal)
    for index in revealed_indexes:
        word_to_display[index] = word_to_guess[index]

    guessed_letters = [word_to_guess[i] for i in revealed_indexes]
    guesses_remaining = 3
    guessed_the_word = False

    print("\n🎮 Time to play Hangman! You have 3 chances.\n")

    while guesses_remaining > 0 and not guessed_the_word:
        print(HANGMANPICS[3 - guesses_remaining])
        print("Word:", ' '.join(word_to_display))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Guesses remaining: {guesses_remaining}\n")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    word_to_display[i] = guess
        else:
            print("❌ Wrong guess!\n")
            guesses_remaining -= 1

        if '_' not in word_to_display:
            guessed_the_word = True
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess)

    if not guessed_the_word:
        print(HANGMANPICS[-1])
        print("💀 Game Over! The word was:", word_to_guess)

if __name__ == '__main__':
    while True:
        play_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye 👋")
            break
