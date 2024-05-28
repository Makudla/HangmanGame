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

def play_game(wordlist):
    word = random.choice(wordlist).lower()

    guessed_word = ["_"] * len(word)
    mistakes = 0
    max_mistakes = 6
    guessed_letters = set()

    print("Zaczynamy grę w wisielca!")

    while mistakes < max_mistakes:
        print(" ".join(guessed_word))
        letter = input("Zgadnij literę: ").lower()

        if letter in guessed_letters:
            print("Już zgadywałeś tę literę.")
        elif letter in word:
            guessed_letters.add(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word[i] = letter
            if "_" not in guessed_word:
                print("Gratulacje! Zgadłeś słowo:", word)
                score = len(set(word)) / (mistakes + 1)
                print(f"Twój wynik: {score:.2f}")
                return score
        else:
            guessed_letters.add(letter)
            mistakes += 1
            draw_hangman(mistakes)
            print(f"Zła litera! Pozostałe próby: {max_mistakes - mistakes}")

    print("Przegrałeś! Słowo to:", word)
    return None
