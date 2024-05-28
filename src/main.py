from game import play_game
from rankings import show_rankings, add_score
from wordlist import add_word, remove_word, display_wordlist
import json
import os

def load_wordlist(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return ["python", "programowanie", "wisielec", "komputer", "nauka"]

def save_wordlist(wordlist, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(wordlist, file)

def main():
    wordlist_file = '../HangmanGame/data/wordlist.json'
    rankings_file = '../HangmanGame/data/rankings.json'

    wordlist = load_wordlist(wordlist_file)

    while True:
        print("\nMenu:")
        print("1. Nowa gra")
        print("2. Sprawdź ranking")
        print("3. Dodaj słowa do listy możliwych")
        print("4. Usuń słowa z listy możliwych")
        print("5. Wyświetl listę słów")
        print("6. Wyjdź z gry")

        choice = input("Wybierz opcję: ")

        if choice == '1':
            score = play_game(wordlist)
            if score is not None:
                while True:
                    nick = input("Podaj swój nick: ")
                    password = input("Podaj swoje hasło: ")

                    if nick and password:  # Sprawdzenie, czy nick i hasło nie są puste
                        success = add_score(rankings_file, nick, password, score)
                        if success:
                            break
                    else:
                        print("Nick i hasło nie mogą być puste. Spróbuj ponownie.")
        elif choice == '2':
            show_rankings(rankings_file)
        elif choice == '3':
            word = input("Podaj nowe słowo: ")
            add_word(wordlist, word)
            save_wordlist(wordlist, wordlist_file)
        elif choice == '4':
            display_wordlist(wordlist)
            try:
                word_index = int(input("Podaj numer słowa do usunięcia: ")) - 1
                remove_word(wordlist, word_index)
                save_wordlist(wordlist, wordlist_file)
            except (ValueError, IndexError):
                print("Nieprawidłowy numer, spróbuj ponownie.")
        elif choice == '5':
            display_wordlist(wordlist)
        elif choice == '6':
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
