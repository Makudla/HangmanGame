import random

def draw_hangman(mistakes):
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ------------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ------------
        """
    ]
    print(hangman_stages[mistakes])

def calculate_score(word, mistakes):
    print("\nGratulacje! Zgadłeś słowo:", word)
    score = len(set(word)) / (mistakes + 1)
    print(f"Twój wynik: {score:.2f}")
    return score
def play_game(wordlist):
    word = random.choice(wordlist).lower()

    guessed_word = ["_"] * len(word)
    mistakes = 0
    max_mistakes = 6
    guessed_letters = set()

    print("\nZaczynamy grę w wisielca!")

    while mistakes < max_mistakes:
        print(" ".join(guessed_word))
        print(" ".join(guessed_letters))
        letter = input("\nZgadnij literę: ").lower()

        if letter == word:
            return calculate_score(word, mistakes)

        if letter in guessed_letters:
            print("Już zgadywałeś tę literę.")
        elif letter in word:
            guessed_letters.add(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
            if "_" not in guessed_word:
                return calculate_score(word, mistakes)
        else:
            guessed_letters.add(letter)
            mistakes += 1
            draw_hangman(mistakes)
            print(f"\nZła litera! Pozostałe próby: {max_mistakes - mistakes}")

    print("\nPRZEGRANA! Słowo to:", word)
    return None
