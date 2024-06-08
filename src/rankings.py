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
    # Szukanie gracza po nicku
    player = next((player for player in rankings if player['nick'] == nick), None)
    if player:
        # Weryfikacja hasła
        if player['password'] == password:
            player['score'] += score
            player['battles'] += 1
            print(f"Punkty zostały dodane do gracza {nick}.")
        else:
            print("Błędne hasło, punkty nie zostały dodane.")
            return False
    else:
        # Dodanie nowego gracza
        battles = 1
        rankings.append({'nick': nick, 'password': password, 'score': score, 'battles': battles})
        print(f"Gracz {nick} został dodany.")
    save_rankings(rankings, filename)
    return True

def show_rankings(filename):
    rankings = load_rankings(filename)
    sorted_rankings = sorted(rankings, key=lambda x: x['score'], reverse=True)
    print("\nRanking:")
    i = 1
    for player in sorted_rankings:
        print(f"[{i}], Nick: {player['nick']}, Wynik: {player['score']:.2f}, Gry: {player['battles']}")
        i += 1

