Marta Kudła s24230
### Opis Projektu Hangman (Wisielec)

Jest to aplikacja konsolowa do gry w wisielca z dodatkowymi funkcjami zarządzania słowami i wynikami graczy. Aplikacja umożliwia graczom rozpoczęcie nowej gry, przeglądanie rankingu najlepszych wyników, dodawanie i usuwanie słów z listy możliwych do odgadnięcia oraz wyświetlanie listy słów. Wyniki graczy są przechowywane w pliku wraz z ich nickami i hasłami, co umożliwia kumulowanie punktów dla poszczególnych graczy.

#### Wymagania:

1. **Rozpoczynanie nowej gry**:
   - Gracz ma możliwość rozpoczęcia nowej gry.
   - Gra losuje słowo z listy możliwych do odgadnięcia.
   - Gracz podaje litery, a gra sprawdza, czy są one poprawne, ignorując wielkość znaków.
   - Gra informuje o liczbie prób, które pozostały, oraz o aktualnym stanie odgadywanego słowa.
   - Po zakończeniu gry (wygrana/przegrana) gracz ma możliwość podania swojego nicku i hasła w celu zapisania wyniku.

2. **Przechowywanie wyników**:
   - Każdy wynik gracza jest przechowywany z jego unikalnym nickiem i hasłem.
   - Wynik jest równy stosunkowi liczby odgadniętych liter do liczby nietrafionych liter.
   - Jeśli gracz istnieje w systemie, musi podać prawidłowe hasło, aby dodać nowy wynik do swojego konta.
   - Jeśli gracz jest nowy, tworzony jest nowy wpis w rankingu z podanym nickiem i hasłem.

3. **Przeglądanie rankingu**:
   - Użytkownik może wyświetlić listę graczy z najwyższymi wynikami.
   - Ranking jest sortowany według wyników graczy w porządku malejącym.

4. **Zarządzanie listą słów**:
   - Użytkownik może dodawać nowe słowa do listy możliwych do odgadnięcia.
   - Użytkownik może usuwać słowa z listy, wybierając je na podstawie indeksu.
   - Użytkownik może wyświetlić aktualną listę słów.

5. **Interaktywny interfejs w konsoli**:
   - Aplikacja zapewnia menu konsolowe z następującymi opcjami:
     1. Nowa gra
     2. Sprawdź ranking
     3. Dodaj słowa do listy możliwych
     4. Usuń słowa z listy możliwych
     5. Wyświetl listę słów
     6. Wyjdź z gry
   - Użytkownik może wybierać różne opcje, wprowadzając odpowiednie numery.

6. **Obsługa błędów**:
   - Aplikacja obsługuje błędy, takie jak podanie nieprawidłowej opcji menu czy niewłaściwego numeru słowa do usunięcia.
   - Użytkownik otrzymuje odpowiednie komunikaty o błędach i jest proszony o ponowne wprowadzenie danych.

#### Struktura Projektu:

- **src/**: Katalog zawierający skrypty programu.
  - `main.py`: Główny skrypt uruchamiający aplikację.
  - `game.py`: Skrypt zawierający logikę gry w wisielca.
  - `rankings.py`: Skrypt zarządzający wynikami graczy.
  - `wordlist.py`: Skrypt zarządzający listą słów.

- **data/**: Katalog zawierający pliki z danymi.
  - `wordlist.json`: Plik przechowujący listę słów.
  - `rankings.json`: Plik przechowujący rankingi graczy.

### Uruchomienie projektu:

1. Otwórz projekt w PyCharm.
2. Upewnij się, że struktura katalogów jest prawidłowa.
3. Uruchom `main.py` w PyCharm.
4. Korzystaj z interaktywnego menu konsolowego, aby zarządzać grą, rankingiem oraz listą słów.

### Przykłady użycia:

- **Nowa gra**: Gracz rozpoczyna nową grę, zgaduje litery słowa i po zakończeniu gry podaje swój nick i hasło, aby zapisać wynik.
- **Sprawdź ranking**: Użytkownik wyświetla aktualny ranking graczy.
- **Dodaj słowa do listy możliwych**: Użytkownik dodaje nowe słowa do listy.
- **Usuń słowa z listy możliwych**: Użytkownik usuwa wybrane słowa z listy, podając ich numery.
- **Wyświetl listę słów**: Użytkownik wyświetla aktualną listę słów dostępnych w grze.

### Podsumowanie:

Projekt Hangman to konsolowa gra w wisielca z rozbudowanymi funkcjami zarządzania słowami i rankingiem graczy. Gra oferuje interaktywne menu, które umożliwia graczom i użytkownikom łatwe zarządzanie różnymi 
 spektami gry, przechowywanie wyników oraz zapewnia przyjazny interfejs użytkownika z odpowiednimi komunikatami o błędach.
