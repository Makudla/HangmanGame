import json
import os

def load_rankings(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_rankings(rankings, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(rankings, file)

def add_score(filename, nick, password, score):
    rankings = load_rankings(filename)
    # Szukamy gracza po nicku
    player = next((player for player in rankings if player['nick'] == nick), None)
    if player:
        # Weryfikacja hasła
        if player['password'] == password:
            player['score'] += score
            print(f"Punkty zostały dodane do gracza {nick}.")
        else:
            print("Błędne hasło, punkty nie zostały dodane.")
            return False
    else:
        # Dodajemy nowego gracza
        player_id = len(rankings) + 1
        rankings.append({'id': player_id, 'nick': nick, 'password': password, 'score': score})
        print(f"Gracz {nick} został dodany.")
    save_rankings(rankings, filename)
    return True

def show_rankings(filename):
    rankings = load_rankings(filename)
    sorted_rankings = sorted(rankings, key=lambda x: x['score'], reverse=True)
    print("\nRanking:")
    for player in sorted_rankings:
        print(f"ID: {player['id']}, Nick: {player['nick']}, Wynik: {player['score']:.2f}")

