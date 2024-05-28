def add_word(wordlist, word):
    if word not in wordlist:
        wordlist.append(word)
        print(f"Słowo '{word}' zostało dodane.")
    else:
        print(f"Słowo '{word}' już istnieje na liście.")

def remove_word(wordlist, index):
    if 0 <= index < len(wordlist):
        removed_word = wordlist.pop(index)
        print(f"Słowo '{removed_word}' zostało usunięte.")
    else:
        print("Nieprawidłowy numer, spróbuj ponownie.")

def display_wordlist(wordlist):
    print("\nLista słów:")
    for i, word in enumerate(wordlist, start=1):
        print(f"[{i}] {word}")
